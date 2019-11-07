# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compareView.ui'
#
# Created: Thu Nov 07 08:04:35 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(2188, 1071)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelDatabase = QtGui.QLabel(self.centralwidget)
        self.labelDatabase.setGeometry(QtCore.QRect(60, 20, 141, 21))
        self.labelDatabase.setObjectName("labelDatabase")
        self.selectDatabase = QtGui.QComboBox(self.centralwidget)
        self.selectDatabase.setGeometry(QtCore.QRect(180, 20, 181, 27))
        self.selectDatabase.setObjectName("selectDatabase")
        self.labelFiles = QtGui.QLabel(self.centralwidget)
        self.labelFiles.setGeometry(QtCore.QRect(60, 50, 70, 21))
        self.labelFiles.setObjectName("labelFiles")
        self.dbFilesTree = QtGui.QTreeView(self.centralwidget)
        self.dbFilesTree.setGeometry(QtCore.QRect(60, 80, 771, 791))
        self.dbFilesTree.setObjectName("dbFilesTree")
        self.widCompare = QtGui.QWidget(self.centralwidget)
        self.widCompare.setEnabled(True)
        self.widCompare.setGeometry(QtCore.QRect(880, 0, 1051, 961))
        self.widCompare.setProperty("hidden", True)
        self.widCompare.setObjectName("widCompare")
        self.resultLenghtSpin = QtGui.QSpinBox(self.widCompare)
        self.resultLenghtSpin.setGeometry(QtCore.QRect(920, 40, 54, 27))
        self.resultLenghtSpin.setObjectName("resultLenghtSpin")
        self.buttonDownload = QtGui.QToolButton(self.widCompare)
        self.buttonDownload.setGeometry(QtCore.QRect(480, 900, 111, 41))
        self.buttonDownload.setObjectName("buttonDownload")
        self.tableResults = QtGui.QTableView(self.widCompare)
        self.tableResults.setGeometry(QtCore.QRect(80, 500, 901, 381))
        self.tableResults.setObjectName("tableResults")
        self.buttonCompare = QtGui.QPushButton(self.widCompare)
        self.buttonCompare.setGeometry(QtCore.QRect(490, 430, 112, 41))
        self.buttonCompare.setObjectName("buttonCompare")
        self.progressBar = QtGui.QProgressBar(self.widCompare)
        self.progressBar.setGeometry(QtCore.QRect(80, 440, 951, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label = QtGui.QLabel(self.widCompare)
        self.label.setGeometry(QtCore.QRect(90, 40, 251, 21))
        self.label.setObjectName("label")
        self.sequenceInput = QtGui.QPlainTextEdit(self.widCompare)
        self.sequenceInput.setGeometry(QtCore.QRect(80, 90, 901, 311))
        self.sequenceInput.setObjectName("sequenceInput")
        self.label_2 = QtGui.QLabel(self.widCompare)
        self.label_2.setGeometry(QtCore.QRect(730, 40, 171, 21))
        self.label_2.setObjectName("label_2")
        self.widMainMenu = QtGui.QWidget(self.centralwidget)
        self.widMainMenu.setGeometry(QtCore.QRect(880, -20, 1051, 961))
        self.widMainMenu.setObjectName("widMainMenu")
        self.buttonMenuEdit = QtGui.QToolButton(self.widMainMenu)
        self.buttonMenuEdit.setGeometry(QtCore.QRect(380, 350, 330, 45))
        self.buttonMenuEdit.setObjectName("buttonMenuEdit")
        self.buttonMenuCompare = QtGui.QPushButton(self.widMainMenu)
        self.buttonMenuCompare.setGeometry(QtCore.QRect(380, 270, 330, 45))
        self.buttonMenuCompare.setObjectName("buttonMenuCompare")
        self.buttonMenuDelete = QtGui.QToolButton(self.widMainMenu)
        self.buttonMenuDelete.setGeometry(QtCore.QRect(380, 510, 330, 45))
        self.buttonMenuDelete.setObjectName("buttonMenuDelete")
        self.buttonMenuAdd = QtGui.QToolButton(self.widMainMenu)
        self.buttonMenuAdd.setGeometry(QtCore.QRect(380, 430, 330, 45))
        self.buttonMenuAdd.setObjectName("buttonMenuAdd")
        self.widAddDB = QtGui.QWidget(self.centralwidget)
        self.widAddDB.setEnabled(True)
        self.widAddDB.setGeometry(QtCore.QRect(880, -50, 1051, 961))
        self.widAddDB.setProperty("hidden", True)
        self.widAddDB.setObjectName("widAddDB")
        self.buttonSelect = QtGui.QPushButton(self.widAddDB)
        self.buttonSelect.setGeometry(QtCore.QRect(400, 320, 251, 41))
        self.buttonSelect.setObjectName("buttonSelect")
        self.progressBar_2 = QtGui.QProgressBar(self.widAddDB)
        self.progressBar_2.setGeometry(QtCore.QRect(80, 550, 951, 23))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.labelDbName = QtGui.QLabel(self.widAddDB)
        self.labelDbName.setGeometry(QtCore.QRect(150, 250, 351, 21))
        self.labelDbName.setObjectName("labelDbName")
        self.inputDbName = QtGui.QLineEdit(self.widAddDB)
        self.inputDbName.setGeometry(QtCore.QRect(500, 250, 391, 27))
        self.inputDbName.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.inputDbName.setObjectName("inputDbName")
        self.labelImport = QtGui.QLabel(self.widAddDB)
        self.labelImport.setGeometry(QtCore.QRect(150, 380, 761, 21))
        self.labelImport.setText("")
        self.labelImport.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImport.setObjectName("labelImport")
        self.labelProcess = QtGui.QLabel(self.widAddDB)
        self.labelProcess.setGeometry(QtCore.QRect(210, 590, 661, 21))
        self.labelProcess.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProcess.setObjectName("labelProcess")
        self.buttonImport = QtGui.QPushButton(self.widAddDB)
        self.buttonImport.setGeometry(QtCore.QRect(400, 450, 251, 41))
        self.buttonImport.setObjectName("buttonImport")
        self.widDeleteDB = QtGui.QWidget(self.centralwidget)
        self.widDeleteDB.setEnabled(True)
        self.widDeleteDB.setGeometry(QtCore.QRect(880, 0, 1051, 961))
        self.widDeleteDB.setProperty("hidden", True)
        self.widDeleteDB.setObjectName("widDeleteDB")
        self.progressBar_3 = QtGui.QProgressBar(self.widDeleteDB)
        self.progressBar_3.setGeometry(QtCore.QRect(80, 550, 951, 23))
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")
        self.labelDbNameDelete = QtGui.QLabel(self.widDeleteDB)
        self.labelDbNameDelete.setGeometry(QtCore.QRect(200, 250, 351, 21))
        self.labelDbNameDelete.setObjectName("labelDbNameDelete")
        self.labelProcessDelete = QtGui.QLabel(self.widDeleteDB)
        self.labelProcessDelete.setGeometry(QtCore.QRect(210, 590, 661, 21))
        self.labelProcessDelete.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProcessDelete.setObjectName("labelProcessDelete")
        self.buttonDelete = QtGui.QPushButton(self.widDeleteDB)
        self.buttonDelete.setGeometry(QtCore.QRect(380, 350, 251, 41))
        self.buttonDelete.setObjectName("buttonDelete")
        self.selectDeleteDatabase = QtGui.QComboBox(self.widDeleteDB)
        self.selectDeleteDatabase.setGeometry(QtCore.QRect(520, 250, 241, 27))
        self.selectDeleteDatabase.setObjectName("selectDeleteDatabase")
        self.askingWidgetDelete = QtGui.QWidget(self.widDeleteDB)
        self.askingWidgetDelete.setGeometry(QtCore.QRect(240, 330, 581, 381))
        self.askingWidgetDelete.setObjectName("askingWidgetDelete")
        self.labelAskDelete = QtGui.QLabel(self.askingWidgetDelete)
        self.labelAskDelete.setGeometry(QtCore.QRect(0, 90, 581, 21))
        self.labelAskDelete.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAskDelete.setObjectName("labelAskDelete")
        self.buttonBox = QtGui.QDialogButtonBox(self.askingWidgetDelete)
        self.buttonBox.setGeometry(QtCore.QRect(170, 140, 231, 31))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonToCompare = QtGui.QPushButton(self.centralwidget)
        self.buttonToCompare.setGeometry(QtCore.QRect(50, 900, 191, 34))
        self.buttonToCompare.setObjectName("buttonToCompare")
        self.buttonToAdd = QtGui.QPushButton(self.centralwidget)
        self.buttonToAdd.setGeometry(QtCore.QRect(250, 900, 191, 34))
        self.buttonToAdd.setObjectName("buttonToAdd")
        self.buttonToEdit = QtGui.QPushButton(self.centralwidget)
        self.buttonToEdit.setGeometry(QtCore.QRect(450, 900, 191, 34))
        self.buttonToEdit.setObjectName("buttonToEdit")
        self.buttonToDelete = QtGui.QPushButton(self.centralwidget)
        self.buttonToDelete.setGeometry(QtCore.QRect(650, 900, 191, 34))
        self.buttonToDelete.setObjectName("buttonToDelete")
        self.widEditDB = QtGui.QWidget(self.centralwidget)
        self.widEditDB.setEnabled(True)
        self.widEditDB.setGeometry(QtCore.QRect(880, 0, 1051, 961))
        self.widEditDB.setProperty("hidden", True)
        self.widEditDB.setObjectName("widEditDB")
        self.buttonDeleteSeq = QtGui.QPushButton(self.widEditDB)
        self.buttonDeleteSeq.setGeometry(QtCore.QRect(380, 210, 251, 41))
        self.buttonDeleteSeq.setObjectName("buttonDeleteSeq")
        self.progressBar_4 = QtGui.QProgressBar(self.widEditDB)
        self.progressBar_4.setGeometry(QtCore.QRect(70, 710, 951, 23))
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setObjectName("progressBar_4")
        self.labelEditProcess = QtGui.QLabel(self.widEditDB)
        self.labelEditProcess.setGeometry(QtCore.QRect(180, 750, 661, 21))
        self.labelEditProcess.setAlignment(QtCore.Qt.AlignCenter)
        self.labelEditProcess.setObjectName("labelEditProcess")
        self.buttonAddSeq = QtGui.QPushButton(self.widEditDB)
        self.buttonAddSeq.setGeometry(QtCore.QRect(390, 650, 251, 41))
        self.buttonAddSeq.setObjectName("buttonAddSeq")
        self.seqContent = QtGui.QTextEdit(self.widEditDB)
        self.seqContent.setGeometry(QtCore.QRect(70, 410, 921, 221))
        self.seqContent.setObjectName("seqContent")
        self.labelSelectedSeq = QtGui.QLabel(self.widEditDB)
        self.labelSelectedSeq.setGeometry(QtCore.QRect(70, 170, 391, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSelectedSeq.sizePolicy().hasHeightForWidth())
        self.labelSelectedSeq.setSizePolicy(sizePolicy)
        self.labelSelectedSeq.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelSelectedSeq.setObjectName("labelSelectedSeq")
        self.newSeqName = QtGui.QLineEdit(self.widEditDB)
        self.newSeqName.setGeometry(QtCore.QRect(70, 360, 241, 27))
        self.newSeqName.setObjectName("newSeqName")
        self.labelSelectedDir = QtGui.QLabel(self.widEditDB)
        self.labelSelectedDir.setGeometry(QtCore.QRect(70, 320, 391, 21))
        self.labelSelectedDir.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelSelectedDir.setObjectName("labelSelectedDir")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2188, 31))
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
        self.buttonDownload.setText(QtGui.QApplication.translate("mainWindow", "Descargar", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonCompare.setText(QtGui.QApplication.translate("mainWindow", "Comparar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("mainWindow", "Ingrese la secuencia a comparar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("mainWindow", "Cantidad de resultados", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonMenuEdit.setText(QtGui.QApplication.translate("mainWindow", "Editar Base de Datos", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonMenuCompare.setText(QtGui.QApplication.translate("mainWindow", "Comparar Secuencias", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonMenuDelete.setText(QtGui.QApplication.translate("mainWindow", "Eliminar base de datos", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonMenuAdd.setText(QtGui.QApplication.translate("mainWindow", "Agregar Base de Datos", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSelect.setText(QtGui.QApplication.translate("mainWindow", "Seleccionar carpeta de archivos", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDbName.setText(QtGui.QApplication.translate("mainWindow", "Ingrese el nombre de la nueva base de datos", None, QtGui.QApplication.UnicodeUTF8))
        self.inputDbName.setPlaceholderText(QtGui.QApplication.translate("mainWindow", "Nombre ", None, QtGui.QApplication.UnicodeUTF8))
        self.labelProcess.setText(QtGui.QApplication.translate("mainWindow", "Importando archivos", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonImport.setText(QtGui.QApplication.translate("mainWindow", "Crear base de datos", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDbNameDelete.setText(QtGui.QApplication.translate("mainWindow", "Seleccione la base de datos a eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.labelProcessDelete.setText(QtGui.QApplication.translate("mainWindow", "Importando archivos", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonDelete.setText(QtGui.QApplication.translate("mainWindow", "Eliminar base de datos", None, QtGui.QApplication.UnicodeUTF8))
        self.labelAskDelete.setText(QtGui.QApplication.translate("mainWindow", "¿Esta seguro que desea eliminar la base de datos? ", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonToCompare.setText(QtGui.QApplication.translate("mainWindow", "Comparar secuencias", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonToAdd.setText(QtGui.QApplication.translate("mainWindow", "Agregar base de datos", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonToEdit.setText(QtGui.QApplication.translate("mainWindow", "Editar base de datos", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonToDelete.setText(QtGui.QApplication.translate("mainWindow", "Eliminar base de datos", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonDeleteSeq.setText(QtGui.QApplication.translate("mainWindow", "Borrar secuencia", None, QtGui.QApplication.UnicodeUTF8))
        self.labelEditProcess.setText(QtGui.QApplication.translate("mainWindow", "Creando archivos", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonAddSeq.setText(QtGui.QApplication.translate("mainWindow", "Agregar secuencia", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSelectedSeq.setText(QtGui.QApplication.translate("mainWindow", "Secuencia seleccionada:", None, QtGui.QApplication.UnicodeUTF8))
        self.newSeqName.setPlaceholderText(QtGui.QApplication.translate("mainWindow", "Nombre de la nueva secuencia", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSelectedDir.setText(QtGui.QApplication.translate("mainWindow", "Carpeta seleccionada:", None, QtGui.QApplication.UnicodeUTF8))

