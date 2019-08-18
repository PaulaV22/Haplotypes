import sys
from PySide import QtGui
from PySide.QtCore import *
from PySide.QtGui import *
import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

app = QtGui.QApplication(sys.argv)

wid = QtGui.QWidget()
wid.resize(screensize[0],screensize[1])
wid.showMaximized()
wid.setWindowTitle('Haplotypes')
wid.show()


sys.exit(app.exec_())