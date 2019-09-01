# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compareView.ui'
#
# Created: Mon Aug 26 22:45:41 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1274, 743)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelDatabase = QtGui.QLabel(self.centralwidget)
        self.labelDatabase.setGeometry(QtCore.QRect(30, 20, 141, 21))
        self.labelDatabase.setObjectName("labelDatabase")
        self.selectDatabase = QtGui.QComboBox(self.centralwidget)
        self.selectDatabase.setGeometry(QtCore.QRect(150, 20, 181, 27))
        self.selectDatabase.setObjectName("selectDatabase")
        self.labelFiles = QtGui.QLabel(self.centralwidget)
        self.labelFiles.setGeometry(QtCore.QRect(30, 60, 70, 21))
        self.labelFiles.setObjectName("labelFiles")
        self.sequenceInput = QtGui.QPlainTextEdit(self.centralwidget)
        self.sequenceInput.setGeometry(QtCore.QRect(630, 70, 591, 161))
        self.sequenceInput.setObjectName("sequenceInput")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(640, 30, 251, 21))
        self.label.setObjectName("label")
        self.buttonCompare = QtGui.QPushButton(self.centralwidget)
        self.buttonCompare.setGeometry(QtCore.QRect(880, 240, 112, 34))
        self.buttonCompare.setObjectName("buttonCompare")
        self.tableResults = QtGui.QTableView(self.centralwidget)
        self.tableResults.setGeometry(QtCore.QRect(630, 290, 591, 391))
        self.tableResults.setObjectName("tableResults")
        self.buttonDownload = QtGui.QToolButton(self.centralwidget)
        self.buttonDownload.setGeometry(QtCore.QRect(1240, 650, 32, 27))
        self.buttonDownload.setObjectName("buttonDownload")
        self.dbFilesTree = QtGui.QTreeView(self.centralwidget)
        self.dbFilesTree.setGeometry(QtCore.QRect(30, 90, 541, 591))
        self.dbFilesTree.setObjectName("dbFilesTree")
        self.resultLenghtSpin = QtGui.QSpinBox(self.centralwidget)
        self.resultLenghtSpin.setGeometry(QtCore.QRect(900, 30, 54, 27))
        self.resultLenghtSpin.setObjectName("resultLenghtSpin")
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(640, 250, 631, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1274, 31))
        self.menubar.setMouseTracking(True)
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDatabase.setText(QtGui.QApplication.translate("mainWindow", "Base de datos", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFiles.setText(QtGui.QApplication.translate("mainWindow", "Archivos", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("mainWindow", "Ingrese la secuencia a comparar", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonCompare.setText(QtGui.QApplication.translate("mainWindow", "Comparar", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonDownload.setText(QtGui.QApplication.translate("mainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))

