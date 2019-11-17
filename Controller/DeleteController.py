from Bio import SeqIO
from PySide.QtGui import *
from PySide.QtCore import *
from View.compareView_ui1 import Ui_mainWindow
import os
import shutil
from Model.HaplotypesSearcher import HaplotypesSearcher as HaplotypeSearcher
from PySide import QtCore, QtGui
from Controller2 import Controller

class DeleteController(Controller.Controller):

    def __init__(self,window):
        Controller.Controller.__init__(self,window)
        self.threadPool = QThreadPool()

    def configureView(self):
        self.selectedDbName=None
        self.window.labelProcessDelete.hide()
        self.window.askingWidgetDelete.hide()
        self.window.buttonDelete.setEnabled(True)
        self.window.buttonDelete.clicked.connect(self.showWidget)
        self.window.progressBar_3.setMinimum(0)
        self.window.progressBar_3.setMaximum(0)
        self.window.progressBar_3.setVisible(False)
        self.window.buttonBox.accepted.connect(self.deleteDb)
        self.window.buttonBox.rejected.connect(self.hideWidget)
        self.setDatabasesOptions()


    def setDatabasesOptions(self):
        self.dbList = self.getDatabases()
        for db in self.dbList:
            self.window.selectDeleteDatabase.addItem(db)

    def removeItem(self):
        self.dbList = self.getDatabases()
        index = self.window.selectDeleteDatabase.findText(self.selectedDbName)
        self.window.selectDeleteDatabase.removeItem(index)
        self.window.selectDatabase.removeItem(index)


    def showWidget(self):
        self.window.labelProcessDelete.hide()
        selectedIndex = self.window.selectDeleteDatabase.currentIndex()
        self.selectedDbName = self.dbList[selectedIndex]
        if (self.selectedDbName):
            self.window.askingWidgetDelete.show()

    def hideWidget(self):
        self.window.askingWidgetDelete.hide()

    def deleteDb(self):
        self.window.labelProcessDelete.setText("Eliminando la base de datos")
        self.window.labelProcessDelete.show()
        self.window.progressBar_3.show()
        self.HS.setDb(self.selectedDbName)
        self.HS.setNewDb(self.selectedDbName)
        self.HS.signals.deleted.connect(self.deletedDb)

        self.HS.setOption("deletedb")
        self.threadPool.start(self.HS)

    def deletedDb(self):
        self.hideWidget()
        self.removeItem()
        self.window.labelProcessDelete.setText("La base de datos ha sido eliminada correctamente ")
        self.window.progressBar_3.hide()

