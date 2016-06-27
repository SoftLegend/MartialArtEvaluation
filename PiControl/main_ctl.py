# -*- coding: utf-8 -*-
__author__ = 'nataniel'

from PyQt4 import QtGui
from main_ui import Ui_Main
from monitor_ctl import Monitor_Ctl

class Main_ctl(QtGui.QDialog):
    def __init__(self):
        super(Main_ctl, self).__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        # Connect events
        self._setupGUI()

    def _setupGUI(self):
        self._setupEvents()
        self.resetGUI()

        self.ui.btnStart.setFocus()

    def _setupEvents(self):
        self.ui.btnReset.clicked.connect(self.resetGUI)
        self.ui.btnStart.clicked.connect(self.start)

    def start(self):
        duration = self.ui.sbDuration.value()
        force = self.ui.sbForce.value()
        nrOfHits = self.ui.sbNrOfHits.value()

        monitor = Monitor_Ctl(duration, nrOfHits, force)
        monitor.center()
        monitor.setModal(True)

        self.hide()
        monitor.exec_()

        self.show()
        self.resetGUI()

    def resetGUI(self):
        self.ui.sbDuration.setValue(60)
        self.ui.sbForce.setValue(1)
        self.ui.sbNrOfHits.setValue(100)
        self.ui.sbDuration.setFocus()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
