import sys
import time
from PyQt4 import QtGui
# Arquivos do projeto
from main_ctl import Main_ctl


class App(object):
    def __init__(self):
        app = QtGui.QApplication(sys.argv)
        self.main = Main_ctl()

        self.main.center()
        self.main.show()

        sys.exit(app.exec_())


if __name__ == "__main__":
    app = App()
