# -*- coding: utf-8 -*-
__author__ = 'nataniel'

from PyQt4 import QtGui, QtCore
from monitor_ui import Ui_Monitor
from results_ctl import Results_Ctl
from threading import Timer
import serial
from time import sleep


class Monitor_Ctl(QtGui.QDialog):
    TIMER_INTERVAL = 0.25

    def __init__(self, duration, nrOfPunches, minimumForce):
        super(Monitor_Ctl, self).__init__()
        self.ui = Ui_Monitor()
        self.ui.setupUi(self)

        # Setup variables
        self.duration = duration
        self.nrOfPunches = nrOfPunches
        self.minimumForce = minimumForce

        self.remainingTime = self.duration
        self.remainingPunches = self.nrOfPunches
        self.maxForce = 0
        self.punches = []
        self.canceled = False

        # Display variables
        self.dispTime = None
        self.dispLastForce = None
        self.dispMaxForce = None
        self.dispRemainingPunches = None


        # Connect events
        self._setupGUI()

        # Initialize USB connection
        self.serial = serial.Serial('/dev/ttyUSB0',
                                    9600,
                                    timeout=0.1,
                                    xonxoff=False,
                                    rtscts=False,
                                    dsrdtr=False)

        self.serial.flushInput()
        self.serial.flushOutput()

        # Initialize timer
        self.initializeTimer()

        # Generating test data
        self.testData = []
        for i in range(0, 100):
            self.testData += [i];

    def _setupGUI(self):
        self._setupEvents()
        self.ui.btnResult.setVisible(False)

    def _setupEvents(self):
        self.connect(self, QtCore.SIGNAL('finished()'), self.showResults)
        self.connect(self, QtCore.SIGNAL('canceled()'), self.close)
        self.connect(self, QtCore.SIGNAL('update()'), self.drawResults)
        self.ui.btnCancel.clicked.connect(self.cancel)

    def cancel(self):
        self.canceled = True

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def drawResults(self):
        self.ui.lblTimeResult.display(self.dispTime)
        self.ui.lblLastForceResult.display(self.dispLastForce)
        self.ui.lblMaxForceResult.display(self.dispMaxForce)
        self.ui.lblPunchesResult.display(self.dispRemainingPunches)


    def initializeTimer(self):
        thread = Timer(self.TIMER_INTERVAL, self.process, ())
        thread.start()

    def showResults(self):
        results = Results_Ctl(self.duration, self.punches)
        results.center()
        results.setModal(True)
        self.hide()

        results.exec_()
        self.close()

    def _readPunch(self):
        # Reading punch
        # TODO: Write logic to read a punch's force
        raw_data = self.serial.readline()
        print(raw_data)
        raw_data = raw_data.strip()

        if raw_data in [None, 'inf']:
            return 0.0

        print(raw_data)

        return float(raw_data)

        # Using test data
        #force = self.testData[0]
        #self.testData = self.testData[1:]

        #return force

    def _isPunch(self, force):
        # Check if it's not noise
        # TODO: Add real value
        isPunch = force >= 0
        return isPunch

    def _evaluatePunch(self, force):
        isValidPunch = False

        # Check if it's a valid punch
        if force >= self.minimumForce:
            isValidPunch = True
            self.remainingPunches -= 1

        # Update maximum force
        if (force > self.maxForce):
            self.maxForce = force

        # Add punch to log
        punch = [self.remainingTime, force, isValidPunch]
        self.punches.append(punch)

        # Debug information
        print("%f\t\t%d\t\t%s" % (self.remainingTime, force, isValidPunch))

        self._updateGUIWithPunch(force)

    def _updateGUIWithPunch(self, force):
        # Update GUI
        self.dispTime = "{0:.2f}".format(self.remainingTime)
        self.dispLastForce = force
        self.dispMaxForce = self.maxForce
        self.dispRemainingPunches = max(self.remainingPunches, 0)

        self.emit(QtCore.SIGNAL('update()'))

    def process(self):
        if self.canceled:
            self.emit(QtCore.SIGNAL('canceled()'))
            return

        # Remaining time
        self.remainingTime -= self.TIMER_INTERVAL

        # Reading punch
        try:
            force = self._readPunch()
        except:
            print("Error reading punch")
            force = 0.0

        if self._isPunch(force):
            self._evaluatePunch(force)

        # Reset timer
        if self.remainingTime > 0:
            thread = Timer(self.TIMER_INTERVAL, self.process, ())
            thread.start()
        else:
            self.emit(QtCore.SIGNAL('finished()'))
