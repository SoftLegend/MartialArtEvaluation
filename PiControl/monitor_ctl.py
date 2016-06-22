# -*- coding: utf-8 -*-
__author__ = 'nataniel'

from PyQt4 import QtGui, QtCore
from monitor_ui import Ui_Monitor
from results_ctl import Results_Ctl
import time
from threading import Timer

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

        # Connect events
        self._setupGUI()

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
        self.ui.btnCancel.clicked.connect(self.cancel)

    def cancel(self):
        self.canceled = True

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def initializeTimer(self):
        thread = Timer(self.TIMER_INTERVAL, self.process, ())
        thread.start()

    def showResults(self):
        results = Results_Ctl(self.punches)
        results.center()
        results.setModal(True)
        self.hide()

        results.exec_()
        self.close()

    def _readPunch(self):
        # Reading punch
        # TODO: Write logic to read a punch's force
        # Using test data
        force = self.testData[0]
        self.testData = self.testData[1:]

        return force

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
        dispTime = "{0:.2f}".format(self.remainingTime)
        dispLastForce = force
        dispMaxForce = self.maxForce
        dispRemainingPunches = max(self.remainingPunches, 0)

        self.ui.lblTimeResult.display(dispTime)
        self.ui.lblLastForceResult.display(dispLastForce)
        self.ui.lblMaxForceResult.display(dispMaxForce)
        self.ui.lblPunchesResult.display(dispRemainingPunches)

    def process(self):
        if self.canceled:
            self.emit(QtCore.SIGNAL('canceled()'))
            return

        # Remaining time
        self.remainingTime -= self.TIMER_INTERVAL

        # Reading punch
        force = self._readPunch()

        if self._isPunch(force):
            self._evaluatePunch(force)

        # Reset timer
        if self.remainingTime > 0:
            thread = Timer(self.TIMER_INTERVAL, self.process, ())
            thread.start()
        else:
            self.emit(QtCore.SIGNAL('finished()'))
