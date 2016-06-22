# -*- coding: utf-8 -*-
__author__ = 'nataniel'

from PyQt4 import QtGui
from results_ui import Ui_Results

class Results_Ctl(QtGui.QDialog):

    def __init__(self, punches):
        super(Results_Ctl, self).__init__()
        self.ui = Ui_Results()
        self.ui.setupUi(self)

        # Connect events
        self._setupEvents()

        # Process results
        self.displayResults(punches)

    def _setupEvents(self):
        self.ui.btnExit.clicked.connect(self.exit)

    def exit(self):
        self.close()

    def displayResults(self, punches):
        pass
        self.ui.lblAvgForceResult.setText(str(len(punches)))

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
