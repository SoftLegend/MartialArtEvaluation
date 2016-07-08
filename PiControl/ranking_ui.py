# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ranking_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Ranking(object):
    def setupUi(self, Ranking):
        Ranking.setObjectName(_fromUtf8("Ranking"))
        Ranking.resize(528, 382)
        self.verticalLayoutWidget = QtGui.QWidget(Ranking)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 511, 371))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.powerRanking = QtGui.QTableWidget(self.verticalLayoutWidget)
        self.powerRanking.setShowGrid(False)
        self.powerRanking.setRowCount(10)
        self.powerRanking.setColumnCount(2)
        self.powerRanking.setObjectName(_fromUtf8("powerRanking"))
        self.horizontalLayout.addWidget(self.powerRanking)
        self.speedRanking = QtGui.QTableWidget(self.verticalLayoutWidget)
        self.speedRanking.setShowGrid(False)
        self.speedRanking.setRowCount(10)
        self.speedRanking.setColumnCount(2)
        self.speedRanking.setObjectName(_fromUtf8("speedRanking"))
        self.horizontalLayout.addWidget(self.speedRanking)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.btnExit = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnExit.setObjectName(_fromUtf8("btnExit"))
        self.verticalLayout.addWidget(self.btnExit)

        self.retranslateUi(Ranking)
        QtCore.QMetaObject.connectSlotsByName(Ranking)

    def retranslateUi(self, Ranking):
        Ranking.setWindowTitle(_translate("Ranking", "Ranking", None))
        self.btnExit.setText(_translate("Ranking", "Exit", None))

