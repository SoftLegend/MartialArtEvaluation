# -*- coding: utf-8 -*-
__author__ = 'nataniel'

from PyQt4 import QtGui, QtCore
from results_ui import Ui_Results
import numpy as np

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


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

        avgForce = round(np.mean(force), 2) # reduce(lambda x, y: x + y, self.punches) / len(self.punches)

        if len(validForce) > 0:
            avgForceValid = round(np.mean(validForce), 2)
        else:
            avgForceValid = 0.0

        maxForce = round(max(force), 2)
        punchesPerSecond = round(len(self.punches) / self.duration, 2)
        validPunchesPerSecond = round(len(validForce) / self.duration, 2)

        self.ui.lblAvgForceResult.setText(str(avgForce))
        self.ui.lblAvgForceValidResult.setText(str(avgForceValid))
        self.ui.lblDurationResult.setText(str(self.duration))
        self.ui.lblMaxForceResult.setText(str(maxForce))
        self.ui.lblPunchesResult.setText(str(len(self.punches)))
        self.ui.lblPunchesValidResult.setText(str(len(validPunches)))
        self.ui.lblPunchesPerSecondResult.setText(str(punchesPerSecond))
        self.ui.lblValidPunchesPerSecondResult.setText(str(validPunchesPerSecond))

        self.ui.label.clear()

        if maxForce < 2:
            self.ui.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/poodle.png")))
        elif maxForce < 4:
            self.ui.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/rabbit.png")))
        elif maxForce < 6:
            self.ui.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/bull.png")))
        elif maxForce < 8:
            self.ui.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/tiger.png")))
        else:
            self.ui.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/t_rex.png")))

        self.ui.label.setScaledContents(True)

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
