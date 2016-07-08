# -*- coding: utf-8 -*-
__author__ = 'nataniel'

from PyQt4 import QtGui, QtCore
from ranking_ui import Ui_Ranking
from constants import POWER_RANKING_FILE, SPEED_RANKING_FILE


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Ranking_Ctl(QtGui.QDialog):

    def __init__(self):
        super(Ranking_Ctl, self).__init__()
        self.ui = Ui_Ranking()
        self.ui.setupUi(self)

        self._setupGUI()

        # Process results
        self.displayRanking()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def exit(self):
        self.close()

    def _setupGUI(self):
        # Connect events
        self._setupEvents()

        self.ui.powerRanking.setHorizontalHeaderItem(0, QtGui.QTableWidgetItem("Name"))
        self.ui.powerRanking.setHorizontalHeaderItem(1, QtGui.QTableWidgetItem("Strength"))

        self.ui.speedRanking.setHorizontalHeaderItem(0, QtGui.QTableWidgetItem("Name"))
        self.ui.speedRanking.setHorizontalHeaderItem(1, QtGui.QTableWidgetItem("Hits/sec"))

    def _setupEvents(self):
        self.ui.btnExit.clicked.connect(self.exit)

    def fillTable(self, table, file):
        f = open(file)
        ranking = f.readlines()
        f.close()
        ranking = [[x.split(',')[0], float(x.split(',')[1])] for x in ranking]

        sorted_ranking = sorted(ranking, key=lambda x: x[1], reverse=True)

        for idx, data in enumerate(sorted_ranking):
            if idx > 9:
                break

            name = data[0]
            value = data[1]

            table.setItem(idx, 0, QtGui.QTableWidgetItem(name))
            table.setItem(idx, 1, QtGui.QTableWidgetItem(str(value)))

    def displayRanking(self):
        self.fillTable(self.ui.powerRanking, POWER_RANKING_FILE)
        self.fillTable(self.ui.speedRanking, SPEED_RANKING_FILE)