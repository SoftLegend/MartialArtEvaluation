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
        Monitor.resize(698, 331)
        self.verticalLayoutWidget = QtGui.QWidget(Monitor)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(340, 10, 351, 311))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblRemainingTime = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblRemainingTime.setObjectName(_fromUtf8("lblRemainingTime"))
        self.horizontalLayout.addWidget(self.lblRemainingTime)
        self.lblTimeResult = QtGui.QLCDNumber(self.verticalLayoutWidget)
        self.lblTimeResult.setMinimumSize(QtCore.QSize(0, 60))
        self.lblTimeResult.setObjectName(_fromUtf8("lblTimeResult"))
        self.horizontalLayout.addWidget(self.lblTimeResult)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblRemainingPunches = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblRemainingPunches.setObjectName(_fromUtf8("lblRemainingPunches"))
        self.horizontalLayout_2.addWidget(self.lblRemainingPunches)
        self.lblPunchesResult = QtGui.QLCDNumber(self.verticalLayoutWidget)
        self.lblPunchesResult.setMinimumSize(QtCore.QSize(0, 60))
        self.lblPunchesResult.setObjectName(_fromUtf8("lblPunchesResult"))
        self.horizontalLayout_2.addWidget(self.lblPunchesResult)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lblLastPunchForce = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblLastPunchForce.setObjectName(_fromUtf8("lblLastPunchForce"))
        self.horizontalLayout_3.addWidget(self.lblLastPunchForce)
        self.lblLastForceResult = QtGui.QLCDNumber(self.verticalLayoutWidget)
        self.lblLastForceResult.setMinimumSize(QtCore.QSize(0, 60))
        self.lblLastForceResult.setObjectName(_fromUtf8("lblLastForceResult"))
        self.horizontalLayout_3.addWidget(self.lblLastForceResult)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lblMaxForce = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblMaxForce.setObjectName(_fromUtf8("lblMaxForce"))
        self.horizontalLayout_4.addWidget(self.lblMaxForce)
        self.lblMaxForceResult = QtGui.QLCDNumber(self.verticalLayoutWidget)
        self.lblMaxForceResult.setMinimumSize(QtCore.QSize(0, 60))
        self.lblMaxForceResult.setObjectName(_fromUtf8("lblMaxForceResult"))
        self.horizontalLayout_4.addWidget(self.lblMaxForceResult)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.btnCancel = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.horizontalLayout_5.addWidget(self.btnCancel)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.label = QtGui.QLabel(Monitor)
        self.label.setGeometry(QtCore.QRect(20, 80, 311, 201))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/poodle.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.lblChangingPlayer = QtGui.QLabel(Monitor)
        self.lblChangingPlayer.setGeometry(QtCore.QRect(10, 10, 681, 311))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblChangingPlayer.sizePolicy().hasHeightForWidth())
        self.lblChangingPlayer.setSizePolicy(sizePolicy)
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
        self.lblChangingPlayer.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(65)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblChangingPlayer.setFont(font)
        self.lblChangingPlayer.setAutoFillBackground(True)
        self.lblChangingPlayer.setObjectName(_fromUtf8("lblChangingPlayer"))
        self.lblComparison = QtGui.QLabel(Monitor)
        self.lblComparison.setGeometry(QtCore.QRect(70, 280, 201, 31))
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
        self.lblComparison.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblComparison.setFont(font)
        self.lblComparison.setObjectName(_fromUtf8("lblComparison"))
        self.lblComparison.raise_()
        self.verticalLayoutWidget.raise_()
        self.label.raise_()
        self.lblChangingPlayer.raise_()

        self.retranslateUi(Monitor)
        QtCore.QMetaObject.connectSlotsByName(Monitor)

    def retranslateUi(self, Monitor):
        Monitor.setWindowTitle(_translate("Monitor", "Monitor", None))
        self.lblRemainingTime.setText(_translate("Monitor", "Remaining time:", None))
        self.lblRemainingPunches.setText(_translate("Monitor", "Remaining punches:", None))
        self.lblLastPunchForce.setText(_translate("Monitor", "Last punch\'s force (kg):", None))
        self.lblMaxForce.setText(_translate("Monitor", "Maximum force (kg):", None))
        self.btnCancel.setText(_translate("Monitor", "Cancel", None))
        self.lblChangingPlayer.setText(_translate("Monitor", "Changing player", None))
        self.lblComparison.setText(_translate("Monitor", "You are winning", None))

