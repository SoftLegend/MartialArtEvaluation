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
    THRESHOLD = 1.2

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
        self.avgForceValidP1 = 0.0
        self.avgForceValidP2 = 0.0
        self.TMP_validPunchesP1 = []
        self.TMP_validPunches = []

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

        if self.isPlayer1Winning():
            self.notifyLosing()
        else:
            self.notifyWinning()

        # Update UI picture
        if self.avgForceValidP2 > 0:
            force = self.avgForceValidP2
        else:
            force = self.avgForceValidP1
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

    def initializeTimer(self):
        thread = Timer(self.TIMER_INTERVAL, self.process, ())
        thread.start()

    def showResults(self):
        # Close serial reader thread
        self.serial.cancel()
        if self.thread is not None:
            self.thread.join()

        enough_punches_p1 = len(self.TMP_validPunchesP1) >= self.nrOfPunches
        enough_punches_p2 = len(self.TMP_validPunches) >= self.nrOfPunches

        player1_won = self.isPlayer1Winning() and enough_punches_p1

        if player1_won:
            player2_won = False
        else:
            player2_won = enough_punches_p2

        results = Results_Ctl(self.nameP1, self.duration, self.punchesP1)
        results.center()
        results.setModal(True)
        if player1_won:
            results.won()
        elif player2_won:
            results.lost()
        else:
            results.draw()

        if self.nameP2.strip() != "":
            results2 = Results_Ctl(self.nameP2, self.duration, self.punches)
            results.moveLeft()
            results2.center()
            results2.setModal(True)
            results2.ui.btnExit.setVisible(False)
            if player2_won:
                results2.won()
            elif player1_won:
                results2.lost()
            else:
                results2.draw()

            results2.show()

        self.hide()
        results.exec_()
        self.close()

    def validPunch(self, val):
        return val[2]

    def isPlayer1Winning(self):
        #if len(self.punchesP1) == 0:
        #    return True


        if self.player2Pending:
            validForceP1 = [x[1] for x in self.TMP_validPunches]
            if len(validForceP1) > 0:
                self.avgForceValidP1 = round(np.mean(validForceP1), 2)
        else:
            validForceP2 = [x[1] for x in self.TMP_validPunches]
            if len(validForceP2) > 0:
                self.avgForceValidP2 = round(np.mean(validForceP2), 2)

        # Store to use in display method

        return self.avgForceValidP1 >= self.avgForceValidP2

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

        print("Sample size = %d\n" % len(split_data))

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

        if isValidPunch:
            self.TMP_validPunches.append(punch)

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
            # Close serial reader thread
            self.serial.cancel()
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
                self.TMP_validPunchesP1 = [x for x in self.TMP_validPunches]
                del self.TMP_validPunches[:]
                self.punchesP1 = [x for x in self.punches]
                del self.punches[:]
                self.maxForce = 0.0
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
