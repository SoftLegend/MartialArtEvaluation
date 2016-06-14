# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitor_ui.ui'
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

class Ui_Monitor(object):
    def setupUi(self, Monitor):
        Monitor.setObjectName(_fromUtf8("Monitor"))
        Monitor.resize(415, 152)
        self.verticalLayoutWidget = QtGui.QWidget(Monitor)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 391, 131))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblRemainingTime = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblRemainingTime.setObjectName(_fromUtf8("lblRemainingTime"))
        self.horizontalLayout.addWidget(self.lblRemainingTime)
        self.lblTimeResult = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblTimeResult.setObjectName(_fromUtf8("lblTimeResult"))
        self.horizontalLayout.addWidget(self.lblTimeResult)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblRemainingPunches = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblRemainingPunches.setObjectName(_fromUtf8("lblRemainingPunches"))
        self.horizontalLayout_2.addWidget(self.lblRemainingPunches)
        self.lblPunchesResult = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblPunchesResult.setObjectName(_fromUtf8("lblPunchesResult"))
        self.horizontalLayout_2.addWidget(self.lblPunchesResult)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lblLastPunchForce = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblLastPunchForce.setObjectName(_fromUtf8("lblLastPunchForce"))
        self.horizontalLayout_3.addWidget(self.lblLastPunchForce)
        self.lblLastForceResult = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblLastForceResult.setObjectName(_fromUtf8("lblLastForceResult"))
        self.horizontalLayout_3.addWidget(self.lblLastForceResult)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lblMaxForce = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblMaxForce.setObjectName(_fromUtf8("lblMaxForce"))
        self.horizontalLayout_4.addWidget(self.lblMaxForce)
        self.lblMaxForceResult = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblMaxForceResult.setObjectName(_fromUtf8("lblMaxForceResult"))
        self.horizontalLayout_4.addWidget(self.lblMaxForceResult)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.btnCancel = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.horizontalLayout_5.addWidget(self.btnCancel)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Monitor)
        QtCore.QMetaObject.connectSlotsByName(Monitor)

    def retranslateUi(self, Monitor):
        Monitor.setWindowTitle(_translate("Monitor", "Monitor", None))
        self.lblRemainingTime.setText(_translate("Monitor", "Remaining time:", None))
        self.lblTimeResult.setText(_translate("Monitor", "TextLabel", None))
        self.lblRemainingPunches.setText(_translate("Monitor", "Remaining punches:", None))
        self.lblPunchesResult.setText(_translate("Monitor", "TextLabel", None))
        self.lblLastPunchForce.setText(_translate("Monitor", "Last punch\'s force (kg):", None))
        self.lblLastForceResult.setText(_translate("Monitor", "TextLabel", None))
        self.lblMaxForce.setText(_translate("Monitor", "Maximum force (kg):", None))
        self.lblMaxForceResult.setText(_translate("Monitor", "TextLabel", None))
        self.btnCancel.setText(_translate("Monitor", "Cancel", None))

