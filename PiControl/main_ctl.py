# -*- coding: utf-8 -*-
__author__ = 'nataniel'

from PyQt4 import QtGui
from main_ui import Ui_Main
from monitor_ctl import Monitor_Ctl
from ranking_ctl import Ranking_Ctl

class Main_ctl(QtGui.QDialog):
    DURATION = 30
    EASY_FORCE = 1
    MEDIUM_FORCE = 2
    HARD_FORCE = 3
    EASY_NR_OF_PUNCHES = 10
    MEDIUM_NR_OF_PUNCHES = 20
    HARD_NR_OF_PUNCHES = 30

    def __init__(self):
        super(Main_ctl, self).__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        # Connect events
        self._setupGUI()

    def _setupGUI(self):
        self._setupEvents()
        self.easyMode()
        self.ui.txtName_P1.setText("Batman")
        self.ui.txtName_P2.setText("Superman")

        self.ui.btnStart.setFocus()

    def _setupEvents(self):
        self.ui.btnStart.clicked.connect(self.start)
        self.ui.btnRanking.clicked.connect(self.showRanking)
        self.ui.btnEasy.clicked.connect(self.easyMode)
        self.ui.btnMedium.clicked.connect(self.mediumMode)
        self.ui.btnHard.clicked.connect(self.hardMode)
        self.ui.btnCustom.clicked.connect(self.customMode)

    def start(self):
        nameP1 = str(self.ui.txtName_P1.text())
        nameP2 = str(self.ui.txtName_P2.text())

        if (nameP1.strip() in ['', ',']) or (nameP2.strip() in ['', ',']):
            return

        duration = self.ui.sbDuration.value()
        force = self.ui.sbForce.value()
        nrOfHits = self.ui.sbNrOfHits.value()

        monitor = Monitor_Ctl(nameP1, nameP2, duration, nrOfHits, force)
        monitor.center()
        monitor.setModal(True)

        self.hide()
        monitor.exec_()

        self.show()

    def configUI(self, duration, force, nrOfHits, disable):
        self.ui.sbDuration.setValue(duration)
        self.ui.sbForce.setValue(force)
        self.ui.sbNrOfHits.setValue(nrOfHits)
        self.ui.sbDuration.setDisabled(disable)
        self.ui.sbForce.setDisabled(disable)
        self.ui.sbNrOfHits.setDisabled(disable)

    def easyMode(self):
        self.configUI(self.DURATION, self.EASY_FORCE, self.EASY_NR_OF_PUNCHES, True)
        self.ui.btnStart.setFocus()

    def mediumMode(self):
        self.configUI(self.DURATION, self.MEDIUM_FORCE, self.MEDIUM_NR_OF_PUNCHES, True)
        self.ui.btnStart.setFocus()

    def hardMode(self):
        self.configUI(self.DURATION, self.HARD_FORCE, self.HARD_NR_OF_PUNCHES, True)
        self.ui.btnStart.setFocus()

    def customMode(self):
        self.configUI(self.DURATION, self.EASY_FORCE, self.EASY_NR_OF_PUNCHES, False)
        self.ui.sbDuration.setFocus()

    def showRanking(self):
        ranking = Ranking_Ctl()
        ranking.center()
        ranking.setModal(True)

        self.hide()
        ranking.exec_()

        self.show()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
