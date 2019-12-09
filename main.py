import sys
from PySide.QtGui import *
from PySide.QtCore import *
from project.Controller.Main import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit(ret)