# -*- coding: utf-8 -*-
__author__ = 'nataniel'

from PyQt4 import QtGui, QtCore
from results_ui import Ui_Results
import numpy as np
from constants import POWER_RANKING_FILE, SPEED_RANKING_FILE

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class Results_Ctl(QtGui.QDialog):

    def __init__(self, name, duration, punches):
        super(Results_Ctl, self).__init__()
        self.ui = Ui_Results()
        self.ui.setupUi(self)
        self.setWindowTitle("Results: " + name)

        self.name = name
        self.duration = duration
        self.punches = punches

        # Connect events
        self._setupEvents()

        # Process results
        self.displayResults()

    def _setupEvents(self):
        self.ui.btnExit.clicked.connect(self.exit)

    def updateRanking(self, force, hitsPerSec):
        f = open(POWER_RANKING_FILE, 'a')
        f.write('%s,%d\n' % (self.name, force))
        f.close()

        f = open(SPEED_RANKING_FILE, 'a')
        f.write('%s,%d\n' % (self.name, hitsPerSec))
        f.close()

    def exit(self):
        self.close()

    def validPunch(self, val):
        return val[2]

    def displayResults(self):
        validPunches = filter(self.validPunch, self.punches)

        force = [x[1] for x in self.punches]
        validForce = [x[1] for x in validPunches]

        avgForce = round(np.mean(force), 2)  # reduce(lambda x, y: x + y, self.punches) / len(self.punches)

        if len(validForce) > 0:
            avgForceValid = round(np.mean(validForce), 2)
        else:
            avgForceValid = 0.0

        maxForce = round(max(force), 2)
        punchesPerSecond = round(len(self.punches) / self.duration, 2)
        validPunchesPerSecond = round(len(validPunches) / self.duration, 2)

        self.updateRanking(maxForce, validPunchesPerSecond)

        self.ui.lblAvgForceResult.setText(str(avgForce))
        self.ui.lblAvgForceValidResult.setText(str(avgForceValid))
        self.ui.lblDurationResult.setText(str(self.duration))
        self.ui.lblMaxForceResult.setText(str(maxForce))
        self.ui.lblPunchesResult.setText(str(len(self.punches)))
        self.ui.lblPunchesValidResult.setText(str(len(validPunches)))
        self.ui.lblPunchesPerSecondResult.setText(str(punchesPerSecond))
        self.ui.lblValidPunchesPerSecondResult.setText(str(validPunchesPerSecond))

        self.ui.label.clear()

        if avgForceValid < 2:
            self.ui.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/poodle.png")))
        elif avgForceValid < 4:
            self.ui.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/rabbit.png")))
        elif avgForceValid < 6:
            self.ui.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/bull.png")))
        elif avgForceValid < 8:
            self.ui.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/tiger.png")))
        else:
            self.ui.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/t_rex.png")))

        self.ui.label.setScaledContents(True)

    def moveLeft(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(0, (screen.height() - size.height()) / 2)

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def won(self):
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.ui.lblWonLost.setPalette(palette)
        self.ui.lblWonLost.setText("You WON!")

    def lost(self):
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.ui.lblWonLost.setPalette(palette)
        self.ui.lblWonLost.setText("You LOST!")
