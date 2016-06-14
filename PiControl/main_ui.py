# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
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

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName(_fromUtf8("Main"))
        Main.resize(300, 164)
        self.verticalLayoutWidget = QtGui.QWidget(Main)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 291, 151))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblDuration = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblDuration.setObjectName(_fromUtf8("lblDuration"))
        self.horizontalLayout.addWidget(self.lblDuration)
        self.sbDuration = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.sbDuration.setMinimum(1)
        self.sbDuration.setMaximum(3600)
        self.sbDuration.setProperty("value", 60)
        self.sbDuration.setObjectName(_fromUtf8("sbDuration"))
        self.horizontalLayout.addWidget(self.sbDuration)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lblForce = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblForce.setObjectName(_fromUtf8("lblForce"))
        self.horizontalLayout_3.addWidget(self.lblForce)
        self.sbForce = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.sbForce.setMinimum(5)
        self.sbForce.setMaximum(1000)
        self.sbForce.setProperty("value", 10)
        self.sbForce.setObjectName(_fromUtf8("sbForce"))
        self.horizontalLayout_3.addWidget(self.sbForce)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblNrOfHits = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblNrOfHits.setObjectName(_fromUtf8("lblNrOfHits"))
        self.horizontalLayout_2.addWidget(self.lblNrOfHits)
        self.sbNrOfHits = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.sbNrOfHits.setMaximum(360000)
        self.sbNrOfHits.setObjectName(_fromUtf8("sbNrOfHits"))
        self.horizontalLayout_2.addWidget(self.sbNrOfHits)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.btnReset = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnReset.setObjectName(_fromUtf8("btnReset"))
        self.horizontalLayout_4.addWidget(self.btnReset)
        self.btnStart = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnStart.setObjectName(_fromUtf8("btnStart"))
        self.horizontalLayout_4.addWidget(self.btnStart)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        Main.setWindowTitle(_translate("Main", "M.A.E.", None))
        self.lblDuration.setText(_translate("Main", "Duration (s):", None))
        self.lblForce.setText(_translate("Main", "Minimum force (kg):", None))
        self.lblNrOfHits.setText(_translate("Main", "Nr. of hits", None))
        self.btnReset.setText(_translate("Main", "Reset", None))
        self.btnStart.setText(_translate("Main", "Start", None))

