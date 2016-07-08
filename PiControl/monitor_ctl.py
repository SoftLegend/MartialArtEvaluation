# -*- coding: utf-8 -*-
__author__ = 'nataniel'

from PyQt4 import QtGui, QtCore
from monitor_ui import Ui_Monitor
from results_ctl import Results_Ctl
from threading import Timer
from serial_reader_thread import SerialReadThread

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Monitor_Ctl(QtGui.QDialog):
    TIMER_INTERVAL = 1
    THRESHOLD = 0.5

    def __init__(self, name, duration, nrOfPunches, minimumForce):
        super(Monitor_Ctl, self).__init__()
        self.ui = Ui_Monitor()
        self.ui.setupUi(self)

        # Setup variables
        self.name = name
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

        # Initialize reader thread
        self.serial = SerialReadThread()
        self.thread = self.serial.start_thread()

        # Initialize timer
        self.initializeTimer()

        # Generating test data
        #self.testData = []
        #for i in range(0, 100):
        #    self.testData += [i];

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

        # Update UI picture
        force = float(self.dispLastForce)

        self.ui.label.clear()

        if force < 2:
            self.ui.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/poodle.png")))
        elif force < 4:
            self.ui.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/rabbit.png")))
        elif force < 6:
            self.ui.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/bull.png")))
        elif force < 8:
            self.ui.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/tiger.png")))
        else:
            self.ui.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/t_rex.png")))

        self.ui.label.setScaledContents(True)

    def initializeTimer(self):
        thread = Timer(self.TIMER_INTERVAL, self.process, ())
        thread.start()

    def showResults(self):
        # Close serial reader thread
        self.serial.cancel()
        if self.thread is not None:
            self.thread.join()

        results = Results_Ctl(self.name, self.duration, self.punches)
        results.center()
        results.setModal(True)
        self.hide()

        results.exec_()
        self.close()

    def _readPunch(self):
        # Reading punch
        raw_data = self.serial.get_data()

        # Split punches
        split_data = []
        done = False

        for data in raw_data:
            if data >= self.THRESHOLD:
                if not done:
                    split_data.append([])
                    done = True
                split_data[-1].append(data)
            else:
                done = False

        if len(split_data) == 0:
            return [0.0]

        res = [0.0] * len(split_data)

        # For each punch, get the maximum value
        for idx, data in enumerate(split_data):
            # Return value in Kg not in g
            res[idx] = float(max(data)) / 1000.0

        # Return list of punches
        return res

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
            punches = self._readPunch()
        except:
            print("Error reading punch")
            punches = []

        for force in punches:
            if self._isPunch(force):
                self._evaluatePunch(force)
            else:
                print("No punch detected")

            self._updateGUIWithPunch(force)

        # Reset timer
        if self.remainingTime > 0:
            thread = Timer(self.TIMER_INTERVAL, self.process, ())
            thread.start()
        else:
            self.emit(QtCore.SIGNAL('finished()'))
