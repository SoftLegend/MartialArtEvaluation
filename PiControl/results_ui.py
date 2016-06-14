# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'results_ui.ui'
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

class Ui_Results(object):
    def setupUi(self, Results):
        Results.setObjectName(_fromUtf8("Results"))
        Results.resize(415, 270)
        self.verticalLayoutWidget = QtGui.QWidget(Results)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 391, 251))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblDuration = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblDuration.setObjectName(_fromUtf8("lblDuration"))
        self.horizontalLayout.addWidget(self.lblDuration)
        self.lblDurationResult = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblDurationResult.setObjectName(_fromUtf8("lblDurationResult"))
        self.horizontalLayout.addWidget(self.lblDurationResult)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblNrOfPunches = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblNrOfPunches.setObjectName(_fromUtf8("lblNrOfPunches"))
        self.horizontalLayout_2.addWidget(self.lblNrOfPunches)
        self.lblPunchesResult = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblPunchesResult.setObjectName(_fromUtf8("lblPunchesResult"))
        self.horizontalLayout_2.addWidget(self.lblPunchesResult)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lblNrOfValidPunches = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblNrOfValidPunches.setObjectName(_fromUtf8("lblNrOfValidPunches"))
        self.horizontalLayout_3.addWidget(self.lblNrOfValidPunches)
        self.lblPunchesValidResult = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblPunchesValidResult.setObjectName(_fromUtf8("lblPunchesValidResult"))
        self.horizontalLayout_3.addWidget(self.lblPunchesValidResult)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.lblPunchesPerSecond = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblPunchesPerSecond.setObjectName(_fromUtf8("lblPunchesPerSecond"))
        self.horizontalLayout_9.addWidget(self.lblPunchesPerSecond)
        self.lblPunchesPerSecondResult = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblPunchesPerSecondResult.setObjectName(_fromUtf8("lblPunchesPerSecondResult"))
        self.horizontalLayout_9.addWidget(self.lblPunchesPerSecondResult)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.lblValidPunchesPerSecond = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblValidPunchesPerSecond.setObjectName(_fromUtf8("lblValidPunchesPerSecond"))
        self.horizontalLayout_10.addWidget(self.lblValidPunchesPerSecond)
        self.lblValidPunchesPerSecondResult = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblValidPunchesPerSecondResult.setObjectName(_fromUtf8("lblValidPunchesPerSecondResult"))
        self.horizontalLayout_10.addWidget(self.lblValidPunchesPerSecondResult)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.lblMaxForce = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblMaxForce.setObjectName(_fromUtf8("lblMaxForce"))
        self.horizontalLayout_7.addWidget(self.lblMaxForce)
        self.lblMaxForceResult = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblMaxForceResult.setObjectName(_fromUtf8("lblMaxForceResult"))
        self.horizontalLayout_7.addWidget(self.lblMaxForceResult)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.lblAvgForce = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblAvgForce.setObjectName(_fromUtf8("lblAvgForce"))
        self.horizontalLayout_8.addWidget(self.lblAvgForce)
        self.lblAvgForceResult = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblAvgForceResult.setObjectName(_fromUtf8("lblAvgForceResult"))
        self.horizontalLayout_8.addWidget(self.lblAvgForceResult)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lblAvgForceValid = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblAvgForceValid.setObjectName(_fromUtf8("lblAvgForceValid"))
        self.horizontalLayout_4.addWidget(self.lblAvgForceValid)
        self.lblAvgForceValidResult = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblAvgForceValidResult.setObjectName(_fromUtf8("lblAvgForceValidResult"))
        self.horizontalLayout_4.addWidget(self.lblAvgForceValidResult)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.btnExit = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnExit.setObjectName(_fromUtf8("btnExit"))
        self.horizontalLayout_5.addWidget(self.btnExit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Results)
        QtCore.QMetaObject.connectSlotsByName(Results)

    def retranslateUi(self, Results):
        Results.setWindowTitle(_translate("Results", "Results", None))
        self.lblDuration.setText(_translate("Results", "Duration (s):", None))
        self.lblDurationResult.setText(_translate("Results", "TextLabel", None))
        self.lblNrOfPunches.setText(_translate("Results", "Nr. of punches:", None))
        self.lblPunchesResult.setText(_translate("Results", "TextLabel", None))
        self.lblNrOfValidPunches.setText(_translate("Results", "Nr. of valid punches:", None))
        self.lblPunchesValidResult.setText(_translate("Results", "TextLabel", None))
        self.lblPunchesPerSecond.setText(_translate("Results", "Punches per second:", None))
        self.lblPunchesPerSecondResult.setText(_translate("Results", "TextLabel", None))
        self.lblValidPunchesPerSecond.setText(_translate("Results", "Valid punches per second:", None))
        self.lblValidPunchesPerSecondResult.setText(_translate("Results", "TextLabel", None))
        self.lblMaxForce.setText(_translate("Results", "Maximum force (kg):", None))
        self.lblMaxForceResult.setText(_translate("Results", "TextLabel", None))
        self.lblAvgForce.setText(_translate("Results", "Avg. force (kg):", None))
        self.lblAvgForceResult.setText(_translate("Results", "TextLabel", None))
        self.lblAvgForceValid.setText(_translate("Results", "Avg. force of valid punches (kg):", None))
        self.lblAvgForceValidResult.setText(_translate("Results", "TextLabel", None))
        self.btnExit.setText(_translate("Results", "Exit", None))

