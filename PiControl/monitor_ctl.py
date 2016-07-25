# -*- coding: utf-8 -*-
__author__ = 'nataniel'

from PyQt4 import QtGui, QtCore
from monitor_ui import Ui_Monitor
from results_ctl import Results_Ctl
from threading import Timer
from serial_reader_thread import SerialReadThread
import numpy as np

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Monitor_Ctl(QtGui.QDialog):
    TIMER_INTERVAL = 1
    PLAYER_CHANGE_INTERVAL = 5
    THRESHOLD = 0.5

    def __init__(self, nameP1, nameP2, duration, nrOfPunches, minimumForce):
        super(Monitor_Ctl, self).__init__()
        self.ui = Ui_Monitor()
        self.ui.setupUi(self)

        # Setup variables
        self.player2Pending = nameP1.strip() != ""
        self.changingPlayer = False
        self.nameP1 = nameP1
        self.nameP2 = nameP2
        self.duration = duration
        self.nrOfPunches = nrOfPunches
        self.minimumForce = minimumForce
        self.punchesP1 = []

        self.remainingTime = self.duration
        self.remainingPunches = self.nrOfPunches
        self.maxForce = 0
        self.punches = []
        self.canceled = False

        # Display variables
        self.dispTime = None
        self.dispLastForce = None
        self.dispMaxForce = None
        self.dispRemainingPunches = None

        # Connect events
        self._setupGUI()

        # Initialize reader thread
        self.serial = SerialReadThread()
        self.thread = self.serial.start_thread()

        # Initialize timer
        self.initializeTimer()

    def _setupGUI(self):
        self._setupEvents()
        self.ui.lblChangingPlayer.setVisible(False)
        self.ui.lblComparison.setVisible(False)

    def _setupEvents(self):
        self.connect(self, QtCore.SIGNAL('finished()'), self.showResults)
        self.connect(self, QtCore.SIGNAL('canceled()'), self.close)
        self.connect(self, QtCore.SIGNAL('update()'), self.drawResults)
        self.connect(self, QtCore.SIGNAL('changedPlayer()'), self.notifyChangedPlayer)
        self.connect(self, QtCore.SIGNAL('changingPlayer()'), self.notifyChangingPlayer)
        self.ui.btnCancel.clicked.connect(self.cancel)

    def notifyWinning(self):
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
        self.ui.lblComparison.setPalette(palette)
        self.ui.lblComparison.setText("You are winning")

    def notifyLosing(self):
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
        self.ui.lblComparison.setPalette(palette)
        self.ui.lblComparison.setText("You are losing")

    def notifyChangedPlayer(self):
        self.ui.lblChangingPlayer.setVisible(False)

    def notifyChangingPlayer(self):
        self.ui.lblComparison.setVisible(True)
        self.ui.lblChangingPlayer.setVisible(True)

    def cancel(self):
        self.canceled = True

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def drawResults(self):
        self.ui.lblTimeResult.display(self.dispTime)
        self.ui.lblLastForceResult.display(self.dispLastForce)
        self.ui.lblMaxForceResult.display(self.dispMaxForce)
        self.ui.lblPunchesResult.display(self.dispRemainingPunches)

        # Update UI picture
        validPunches = filter(self.validPunch, self.punches)
        validForce = [x[1] for x in validPunches]
        force = 0.0

        if len(validForce) > 0:
            force = round(np.mean(validForce), 2)

        self.ui.label.clear()

        if force < 2:
            self.ui.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/poodle.png")))
        elif force < 4:
            self.ui.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/rabbit.png")))
        elif force < 6:
            self.ui.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/bull.png")))
        elif force < 8:
            self.ui.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/tiger.png")))
        else:
            self.ui.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/t_rex.png")))

        self.ui.label.setScaledContents(True)

        if self.isPlayer1Winning():
            self.notifyLosing()
        else:
            self.notifyWinning()

    def initializeTimer(self):
        thread = Timer(self.TIMER_INTERVAL, self.process, ())
        thread.start()

    def showResults(self):
        # Close serial reader thread
        self.serial.cancel()
        if self.thread is not None:
            self.thread.join()

        player1Won = self.isPlayer1Winning()

        results = Results_Ctl(self.nameP1, self.duration, self.punchesP1)
        results.center()
        results.setModal(True)
        if player1Won:
            results.won()
        else:
            results.lost()

        if self.nameP2.strip() != "":
            results2 = Results_Ctl(self.nameP2, self.duration, self.punches)
            results.moveLeft()
            results2.center()
            results2.setModal(True)
            results2.ui.btnExit.setVisible(False)
            if not player1Won:
                results2.won()
            else:
                results2.lost()
            results2.show()

        self.hide()
        results.exec_()
        self.close()

    def validPunch(self, val):
        return val[2]

    def isPlayer1Winning(self):
        if len(self.punchesP1) == 0:
            return True

        validPunchesP1 = filter(self.validPunch, self.punchesP1)
        validForceP1 = [x[1] for x in validPunchesP1]
        avgForceValidP1 = 0.0
        avgForceValidP2 = 0.0

        if len(validForceP1) > 0:
            avgForceValidP1 = round(np.mean(validForceP1), 2)

        validPunchesP2 = filter(self.validPunch, self.punches)
        validForceP2 = [x[1] for x in validPunchesP2]
        if len(validForceP2) > 0:
            avgForceValidP2 = round(np.mean(validForceP2), 2)

        return avgForceValidP1 >= avgForceValidP2

    def _readPunch(self):
        # Reading punch
        raw_data = self.serial.get_data()

        # Split punches
        split_data = []
        done = False

        for data in raw_data:
            if data >= self.THRESHOLD:
                if not done:
                    split_data.append([])
                    done = True
                split_data[-1].append(data)
            else:
                done = False

        if len(split_data) == 0:
            return [0.0]

        res = [0.0] * len(split_data)

        # For each punch, get the maximum value
        for idx, data in enumerate(split_data):
            # Return value in Kg not in g
            res[idx] = float(max(data)) / 1000.0

        # Return list of punches
        return res

    def _isPunch(self, force):
        # Check if it's not noise
        # TODO: Add real value
        isPunch = force >= 0
        return isPunch

    def _evaluatePunch(self, force):
        isValidPunch = False

        # Check if it's a valid punch
        if force >= self.minimumForce:
            isValidPunch = True
            self.remainingPunches -= 1

        # Update maximum force
        if (force > self.maxForce):
            self.maxForce = force

        # Add punch to log
        punch = [self.remainingTime, force, isValidPunch]
        self.punches.append(punch)

        # Debug information
        print("%f\t\t%d\t\t%s" % (self.remainingTime, force, isValidPunch))

    def _updateGUIWithPunch(self, force):
        # Update GUI
        self.dispTime = "{0:.2f}".format(self.remainingTime)
        self.dispLastForce = force
        self.dispMaxForce = self.maxForce
        self.dispRemainingPunches = max(self.remainingPunches, 0)

        self.emit(QtCore.SIGNAL('update()'))

    def process(self):
        if self.canceled:
            self.emit(QtCore.SIGNAL('canceled()'))
            return

        # Remaining time
        self.remainingTime -= self.TIMER_INTERVAL

        if not self.changingPlayer:
            # Reading punch
            try:
                punches = self._readPunch()
            except:
                print("Error reading punch")
                punches = []

            for force in punches:
                if self._isPunch(force):
                    self._evaluatePunch(force)
                else:
                    print("No punch detected")

                self._updateGUIWithPunch(force)

        # Reset timer
        if self.remainingTime > 0:
            thread = Timer(self.TIMER_INTERVAL, self.process, ())
            thread.start()
        else:
            if self.player2Pending:
                # Reset variables for player 2
                self.player2Pending = False
                self.remainingPunches = self.nrOfPunches
                self.remainingTime = self.PLAYER_CHANGE_INTERVAL
                self.punchesP1 = self.punches
                self.punches = []
                self.dispTime = 0.0
                self.dispLastForce = 0.0
                self.dispMaxForce = 0.0
                self.dispRemainingPunches = 0
                self.changingPlayer = True

                # Emit player changing signal and wait
                self.emit(QtCore.SIGNAL('changingPlayer()'))
                thread = Timer(self.TIMER_INTERVAL, self.process, ())
                thread.start()
            elif self.changingPlayer:
                # Emit player changed signal and start new timer
                self.remainingTime = self.duration
                self.changingPlayer = False
                self.dispTime = self.duration
                self.dispRemainingPunches = self.nrOfPunches
                self.emit(QtCore.SIGNAL('changedPlayer()'))
                thread = Timer(self.TIMER_INTERVAL, self.process, ())
                thread.start()
            else:
                self.emit(QtCore.SIGNAL('finished()'))
