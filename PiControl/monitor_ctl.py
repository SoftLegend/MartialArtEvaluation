# -*- coding: utf-8 -*-
__author__ = 'nataniel'

from PyQt4 import QtGui
from monitor_ui import Ui_Monitor
from results_ctl import Results_Ctl
import time
from threading import Timer

class Monitor_Ctl(QtGui.QDialog):
    TIMER_INTERVAL = 1

    def __init__(self, parent, duration, nrOfPunches, minimumForce):
        super(Monitor_Ctl, self).__init__()
        self.parent = parent
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

        # Connect events
        self._setupEvents()

        # Initialize timer
        self.initializeTimer()

        # Generating test data
        self.testData = []
        for i in range(0, 10):
            self.testData += [i];

    def _setupEvents(self):
        self.ui.btnCancel.clicked.connect(self.cancel)

    def cancel(self):
        pass

    #def returnToMain(self):
    #    self.parent.show()
    #    self.close()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def initializeTimer(self):
        thread = Timer(self.TIMER_INTERVAL, self.process, ())
        thread.start()

    def process(self):
        # Remaining time
        self.remainingTime -= self.TIMER_INTERVAL

        # Reading punch
        # TODO: Write logic to read a punch's force
        # Using test data
        force = self.testData[0]
        self.testData = self.testData[1:]

        # Check if it's not noise
        # TODO: Add real value
        isPunch = force >= 0

        if (isPunch):
            isValidPunch = False
            # Check if it's a valid punch
            if (force >= self.minimumForce):
                isValidPunch = True
                self.remainingPunches -= 1

            # Update maximum force
            if (force > self.maxForce):
                self.maxForce = force

            punch = [self.remainingTime, force, isValidPunch]
            self.punches.append(punch)

            # Debug...
            print("%f\t\t%s" % (self.remainingTime, time.time()))

            # Update GUI
            dispTime = str(self.remainingTime)
            dispLastForce = str(force)
            dispMaxForce = str(self.maxForce)
            dispRemainingPunches = str(max(self.remainingPunches, 0))

            self.ui.lblTimeResult.setText(dispTime)
            self.ui.lblLastForceResult.setText(dispLastForce)
            self.ui.lblMaxForceResult.setText(dispMaxForce)
            self.ui.lblPunchesResult.setText(dispRemainingPunches)

        # Reset timer
        if (self.remainingTime > 0):
            thread = Timer(self.TIMER_INTERVAL, self.process, ())
            thread.start()
        else:
            self.showResults()

    def showResults(self):
        self.results = Results_Ctl(self, self.punches)
        self.results.center()
        self.results.setModal(True)
        #self.hide()
        self.results.exec_()

        #self.close()