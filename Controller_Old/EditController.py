import sys
import os
from PySide.QtGui import *
from PySide.QtCore import *
from View.compareView_ui import Ui_mainWindow
from Model.HaplotypesSearcher import HaplotypesSearcher as HaplotypeSearcher

class EditController:

    def __init__(self, widget):
        self.widget = widget
        self.threadPool = QThreadPool()
        self.HS = HaplotypeSearcher()

    def configureEditView(self):
        self.widget.labelSelectedSeq.show()
        self.widget.buttonDeleteSeq.setEnabled(False)
        self.widget.newSeqName.setEnabled(True)
        self.widget.newSeqName.textChanged.connect(self.checkSeqName)
        self.widget.seqContent.setEnabled(True)
        self.widget.seqContent.textChanged.connect(self.checkSeqContent)
        self.widget.buttonAddSeq.setEnabled(False)
        self.widget.progressBar_4.hide()
        self.widget.labelEditProcess.hide()
        self.widget.dbFilesTree.doubleClicked.connect(self.configure)
        self.widget.selectDatabase.currentIndexChanged.connect(self.changeDb)
        self.widget.buttonDeleteSeq.clicked.connect(self.deleteSeq)
        self.widget.buttonAddSeq.clicked.connect(self.addSeq)
        self.widget.progressBar_4.setMinimum(0)
        self.widget.progressBar_4.setMaximum(0)
        self.widget.progressBar_4.setVisible(False)

    def changeDb(self):
        self.dbList = self.HS.getDatabases()
        self.projectPath= self.HS.getProjectPath()
        selectedIndex = self.widget.selectDatabase.currentIndex()
        dbName = self.dbList[selectedIndex]
        if dbName:
            self.path = self.projectPath + '\Databases\\' + dbName
        else:
            if len(self.dbList) > 0:
                self.path = self.projectPath + '\Databases\\' + self.dbList[0]
        self.widget.labelSelectedDir.setText("Carpeta seleccionada: " + self.path)
        self.checkSeqName()

    def setFileModel(self,filemodel):
        self.filemodel = filemodel

    def configure(self):
        index = self.widget.dbFilesTree.currentIndex()
        path = (self.filemodel.filePath(index))
        path2 = path.replace(" ","_")
        self.widget.labelEditProcess.hide()
        if os.path.isfile(path2):
            self.toDelete = path2
            self.widget.labelSelectedSeq.setText("Secuencia seleccionada: "+path)
            self.widget.labelSelectedDir.setText("Carpeta seleccionada: ")
            self.widget.buttonDeleteSeq.setEnabled(True)
            self.widget.buttonAddSeq.setEnabled(False)
        else:
            self.path = path2
            self.widget.labelSelectedDir.setText("Carpeta seleccionada: "+path)
            self.widget.labelSelectedSeq.setText("Secuencia seleccionada: ")
            self.widget.buttonDeleteSeq.setEnabled(False)
            self.widget.newSeqName.setEnabled(True)
            self.widget.seqContent.setEnabled(True)
            self.widget.buttonAddSeq.setEnabled(True)

    def validSeq(self, seq):
        for base in seq:
            if base not in "ATGC":
                 return False
        return True

    def checkSeqName(self):
        newSeqPath = self.path+"/"+ self.widget.newSeqName.text()+".fa"
        if os.path.exists(newSeqPath):
            self.widget.buttonAddSeq.setEnabled(False)
            self.widget.labelEditProcess.setText("Ya existe una secuencia con ese nombre en el directorio seleccionado")
            self.widget.labelEditProcess.show()
        else:
            self.widget.labelEditProcess.setText("")
            self.widget.labelEditProcess.hide()
            self.checkSeqContent()

    def checkSeqContent(self):
        self.seqContent = self.widget.seqContent.toPlainText()
        self.seqContent =  self.seqContent.replace('\n', '')
        self.seqContent =  self.seqContent.replace('\t', '')
        self.seqName = self.widget.newSeqName.text()
        valid = False
        if self.seqContent!="" and self.validSeq(self.seqContent):
            valid = True
        if self.seqContent!="" and self.validSeq(self.seqContent) and self.seqName!= "":
            print("valid seq")
            self.widget.buttonAddSeq.setEnabled(True)
            self.widget.labelEditProcess.setText("El contenido de la secuencia debe contener las letras A C T G")

        else:
            if not self.validSeq(self.seqContent):
                self.widget.buttonAddSeq.setEnabled(False)
                self.widget.labelEditProcess.setText("El contenido de la secuencia debe contener las letras A C T G")
                self.widget.labelEditProcess.show()

    def dbReady(self):
        self.widget.labelEditProcess.setText("Secuencia eliminada correctamente")
        self.widget.labelEditProcess.show()
        self.widget.buttonDeleteSeq.setEnabled(False)
        self.widget.buttonAddSeq.setEnabled(False)

    def getDb(self):
        self.dbList = self.HS.getDatabases()
        selectedIndex = self.widget.selectDatabase.currentIndex()
        dbName = self.dbList[selectedIndex]
        return dbName

    def deleteSeq(self):
        dbName = self.getDb()
        self.widget.progressBar_4.show()
        self.widget.progressBar_4.repaint()
        self.widget.labelEditProcess.setText("Eliminando secuencia")
        self.widget.labelEditProcess.show()
        self.HS = HaplotypeSearcher(dbName)
        self.HS.signals.deletedSeq.connect(self.dbReady)
        self.HS.setOption("deleteSeq")
        self.HS.setSequenceToDelete(self.toDelete)
        self.threadPool.start(self.HS)

    def newSeqReady(self):
        self.widget.labelEditProcess.setText("Secuencia agregada correctamente")
        self.widget.labelEditProcess.show()
        self.widget.buttonDeleteSeq.setEnabled(False)
        self.widget.buttonAddSeq.setEnabled(False)

    def addSeq(self):
        dbName = self.getDb()
        self.widget.progressBar_4.show()
        self.widget.progressBar_4.repaint()
        self.widget.labelEditProcess.setText("Agregando secuencia")
        self.widget.labelEditProcess.show()
        self.HS = HaplotypeSearcher(dbName)
        self.HS.signals.addedSeq.connect(self.newSeqReady)
        self.HS.setOption("addSeq")
        self.HS.setAddSeqValues(self.path, self.seqContent, self.seqName)
        self.threadPool.start(self.HS)
