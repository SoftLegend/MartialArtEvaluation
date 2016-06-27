# -*- coding: utf-8 -*-
__author__ = 'nataniel'

from PyQt4 import QtGui
from results_ui import Ui_Results
import numpy as np

class Results_Ctl(QtGui.QDialog):

    def __init__(self, duration, punches):
        super(Results_Ctl, self).__init__()
        self.ui = Ui_Results()
        self.ui.setupUi(self)

        self.duration = duration
        self.punches = punches

        # Connect events
        self._setupEvents()

        # Process results
        self.displayResults()

    def _setupEvents(self):
        self.ui.btnExit.clicked.connect(self.exit)

    def exit(self):
        self.close()

    def validPunch(self, val):
        return val[2]

    def displayResults(self):
        validPunches = filter(self.validPunch, self.punches)

        force = [x[1] for x in self.punches]
        validForce = [x[1] for x in validPunches]

        avgForce = np.mean(force) # reduce(lambda x, y: x + y, self.punches) / len(self.punches)
        avgForceValid = np.mean(validForce)

        maxForce = max(force)
        punchesPerSecond = len(self.punches) / self.duration
        validPunchesPerSecond = len(validForce) / self.duration

        self.ui.lblAvgForceResult.setText(str(avgForce))
        self.ui.lblAvgForceValidResult.setText(str(avgForceValid))
        self.ui.lblDurationResult.setText(str(self.duration))
        self.ui.lblMaxForceResult.setText(str(maxForce))
        self.ui.lblPunchesResult.setText(str(len(self.punches)))
        self.ui.lblPunchesValidResult.setText(str(len(validPunches)))
        self.ui.lblPunchesPerSecondResult.setText(str(punchesPerSecond))
        self.ui.lblValidPunchesPerSecondResult.setText(str(validPunchesPerSecond))

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
