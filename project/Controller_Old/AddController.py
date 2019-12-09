from Bio import SeqIO
from PySide.QtGui import *
from PySide.QtCore import *
import os
import shutil
from Model.HaplotypesSearcher import HaplotypesSearcher as HaplotypeSearcher

class AddController:

    def __init__(self, widAddDB):
        self.widget = widAddDB
        self.threadPool = QThreadPool()

    def configureAddView(self):
        self.fileName=None
        self.widget.labelProcess.hide()
        self.widget.labelImport.hide()
        self.widget.buttonSelect.clicked.connect(self.importFiles)
        self.widget.buttonImport.setEnabled(False)
        self.widget.buttonImport.clicked.connect(self.copyFiles)
        self.widget.inputDbName.textChanged.connect(self.enableButton)
        self.widget.progressBar_2.setMinimum(0)
        self.widget.progressBar_2.setMaximum(0)
        self.widget.progressBar_2.setVisible(False)
        self.projectPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def importFiles(self):
        self.fileName = QFileDialog().getExistingDirectory(None, '',QDir.homePath(), QFileDialog.ShowDirsOnly)
        if self.fileName:
            if (os.path.isdir(self.fileName)):
                self.widget.labelImport.setText("Carpeta seleccionada: "+self.fileName)
                self.widget.labelImport.show()
                if self.widget.inputDbName.text()!="":
                    self.widget.buttonImport.setEnabled(True)

    def enableButton(self):
        if self.widget.inputDbName.text()!="":
            if not self.fileName is None:
                self.widget.buttonImport.setEnabled(True)
                return
        self.widget.buttonImport.setEnabled(False)

    def makeDir(self, path):
        if not os.path.exists(path):
            print ("creo el directorio "+ path)
            os.makedirs(path)

    def isFastaFile(self,file, filepath):
        extension = os.path.splitext(file)[1]
        if extension==".fa" or extension==".fasta":
            with open(filepath, "r") as handle:
                fasta = SeqIO.parse(handle, "fasta")
                return any(fasta)  # False when `fasta` is empty, i.e. wasn't a FASTA file
        return False

    def copyFiles(self):
        self.dbName = self.widget.inputDbName.text()
        dbPath = self.projectPath+"/Databases/"+self.dbName
        self.makeDir(dbPath)
        self.widget.progressBar_2.show()
        self.widget.progressBar_2.repaint()
        self.widget.labelProcess.setText("Copiando archivos a directorio del programa")
        self.widget.labelProcess.show()
        for bases, dirs, files in os.walk(self.fileName):
            for file in files:
                sequenceOrigin = bases + '/' + file
                pathDest = dbPath+bases[len(self.fileName):]
                sequenceDest =  pathDest + '/' + file
                self.makeDir(pathDest)
                if not self.isFastaFile(file,sequenceOrigin):
                    self.widget.labelProcess.setText("ERROR: El archivo "+ file+ " no posee el formato Fasta necesario")
                    self.widget.labelProcess.show()
                    return
                #print(sequenceOrigin+ "--> "+ sequenceDest)
                if os.path.exists(sequenceOrigin):
                    shutil.copy2(sequenceOrigin, sequenceDest)
                    print("Archivo copiado")
        self.widget.labelProcess.setText("Configurando bases de datos en el sistema")
        self.HS = HaplotypeSearcher(self.dbName)
        self.HS.setNewDb(self.dbName)
        self.HS.signals.database.connect(self.dbReady)
        self.HS.setNewDb(self.dbName)
        self.HS.setOption("configuredb")
        self.threadPool.start(self.HS)

    def dbReady(self):
        self.widget.labelProcess.setText("La base de datos fue agregada correctamente")
        self.widget.progressBar_2.hide()
        self.widget.selectDatabase.addItem(self.dbName)

