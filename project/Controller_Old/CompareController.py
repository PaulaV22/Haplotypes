from Model import *
import sys
import os
from PySide.QtGui import *
from PySide.QtCore import *
from project.View import Ui_mainWindow
import numpy as np
from Model import *
from Model.HaplotypesSearcher import HaplotypesSearcher as HaplotypeSearcher
from Controller_Old import AddController as AC
from Controller_Old import DeleteController as DC
from Controller_Old import EditController as EC

class CustomTableModel(QAbstractTableModel):
    def __init__(self, data=None):
        QAbstractTableModel.__init__(self)
        self.load_data(data)

    def load_data(self, data):
        if len(data)>1:
            self.input_seqs = data[:,0]
            self.input_score = data[:,1]
            self.input_evalue = data[:,2]
            self.input_percent = data[:,5]
            self.column_count = 4
            self.row_count = len(self.input_seqs)
        else:
            self.column_count = 4
            self.row_count = 0

    def rowCount(self, parent=QModelIndex()):
        return self.row_count

    def columnCount(self, parent=QModelIndex()):
        return self.column_count

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return ("Combinacion", "Score", "E-Value","% Similitud")[section]
        else:
            return "{}".format(section)

    def data(self, index, role = Qt.DisplayRole):
        column = index.column()
        row = index.row()
        if role == Qt.DisplayRole:
            if column == 0:
                return self.input_seqs[row]
            elif column == 1:
                return self.input_score[row]
            elif column == 2:
                return self.input_evalue[row]
            elif column == 3:
                return self.input_percent[row]
        elif role == Qt.BackgroundRole:
            return QColor(Qt.white)
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignRight
        return None

class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.dbFilesTree =QTreeView(self)
        self.dbFilesTree.setGeometry(QRect(60, 80, 771, 791))
        self.dbFilesTree.setObjectName("dbFilesTree")
        self.projectPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.widCompare.hide()
        self.widAddDB.hide()
        self.widDeleteDB.hide()
        self.addController = AC.AddController(self)
        self.buttonMenuAdd.clicked.connect(self.changeToAdd)
        self.addController.configureAddView()
        self.deleteController = DC.DeleteController(self)
        self.deleteController.configureDeleteView()
        self.editController = EC.EditController(self)
        self.editController.configureEditView()
        self.buttonMenuDelete.clicked.connect(self.changeToDelete)
        self.buttonCompare.clicked.connect(self.changeToCompare)
        self.buttonMenuEdit.clicked.connect(self.changeToEdit)
        self.show()
        self.HS = HaplotypeSearcher()
        self.dbList = self.HS.getDatabases()
        self.dbName =""
        self.setDatabases()
        self.selectDatabase.currentIndexChanged.connect(self.changeTreeFiles)
        self.setDatabase()
        self.drawTable([[]])
        self.buttonCompare.clicked.connect(self.compare)
        self.resultLenghtSpin.setValue(10)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self.progressBar.setVisible(False)
        self.threadPool = QThreadPool()
        #self.HS.signals.result.__call__(self.showResults)
        self.HS.signals.updatedatabases.connect(self.dbReady)
        self.HS.signals.result.connect(self.showResults)
        self.buttonMenuCompare.clicked.connect(self.changeToCompare)
        self.changeToMain()
        self.buttonToCompare.clicked.connect(self.changeToCompare)
        self.buttonToDelete.clicked.connect(self.changeToDelete)
        self.buttonToAdd.clicked.connect(self.changeToAdd)
        self.buttonToEdit.clicked.connect(self.changeToEdit)


    def printevent(self):
        print(self.dbFilesTree.model())

    def setDatabases(self):
        self.dbList = self.HS.getDatabases()
        for db in self.dbList:
            self.selectDatabase.addItem(db)

    def changeToCompare(self):
        self.buttonToAdd.setEnabled(True)
        self.buttonToAdd.show()
        self.buttonToCompare.setEnabled(False)
        self.buttonToCompare.show()
        self.buttonToDelete.setEnabled(True)
        self.buttonToDelete.show()
        self.buttonToEdit.setEnabled(True)
        self.buttonToEdit.show()
        self.widMainMenu.hide()
        self.widDeleteDB.hide()
        self.widAddDB.hide()
        self.widEditDB.hide()
        self.widCompare.show()

    def changeToEdit(self):
        self.buttonToAdd.setEnabled(True)
        self.buttonToAdd.show()
        self.buttonToCompare.setEnabled(True)
        self.buttonToCompare.show()
        self.buttonToDelete.setEnabled(True)
        self.buttonToDelete.show()
        self.buttonToEdit.setEnabled(False)
        self.buttonToEdit.show()
        self.widMainMenu.hide()
        self.widDeleteDB.hide()
        self.widAddDB.hide()
        self.widCompare.hide()
        self.widEditDB.show()

    def changeToAdd(self):
        self.widMainMenu.hide()
        self.widDeleteDB.hide()
        self.widCompare.hide()
        self.widAddDB.show()
        self.buttonToAdd.setEnabled(False)
        self.buttonToAdd.show()
        self.buttonToCompare.setEnabled(True)
        self.buttonToCompare.show()
        self.buttonToDelete.setEnabled(True)
        self.buttonToDelete.show()
        self.buttonToEdit.setEnabled(True)
        self.widEditDB.hide()
        self.buttonToEdit.show()

    def changeToDelete(self):
        self.widMainMenu.hide()
        self.widCompare.hide()
        self.widAddDB.hide()
        self.widDeleteDB.show()
        self.buttonToAdd.setEnabled(True)
        self.buttonToAdd.show()
        self.buttonToCompare.setEnabled(True)
        self.buttonToCompare.show()
        self.buttonToDelete.setEnabled(False)
        self.buttonToDelete.show()
        self.buttonToEdit.setEnabled(True)
        self.widEditDB.hide()
        self.buttonToEdit.show()

    def changeToMain(self):
        self.widCompare.hide()
        self.widAddDB.hide()
        self.widDeleteDB.hide()
        self.buttonToAdd.setEnabled(True)
        self.buttonToAdd.hide()
        self.buttonToCompare.setEnabled(True)
        self.buttonToCompare.hide()
        self.buttonToDelete.setEnabled(True)
        self.buttonToDelete.hide()
        self.buttonToEdit.setEnabled(True)
        self.buttonToEdit.hide()
        self.widEditDB.hide()
        self.widMainMenu.show()



    def showResults(self, results):
        print(results)
        dt = np.dtype('string', 'float', 'int')

        resultsArray = np.array(results, dtype=dt)
        print(resultsArray)
        model = CustomTableModel(resultsArray)
        # Creating a QTableView
        self.tableResults.setModel(model)
        self.progressBar.hide()
        self.buttonCompare.show()
        # self.drawTable(results)

    def setDatabase(self):
        if not self.dbList:
            self.dbList = self.HS.getDatabases()
        if self.dbName =="":
            self.dbName = self.HS.getDbName()
        selectedDb = ""
        if self.dbName in self.dbList:
            selectedDb = self.projectPath + '\Databases\\' + self.dbName
        else:
            if len(self.dbList)>0:
                selectedDb = self.projectPath+'\Databases\\'+self.dbList[0]
        if (selectedDb!=""):
            self.filemodel = QFileSystemModel()
            self.filemodel.setRootPath(selectedDb)
            self.dbFilesTree.setModel(self.filemodel)
            self.editController.setFileModel(self.filemodel)
            indexRoot = self.filemodel.index(self.filemodel.rootPath())
            self.dbFilesTree.setRootIndex(indexRoot)

    def changeTreeFiles(self):
        self.dbList = self.HS.getDatabases()
        selectedIndex = self.selectDatabase.currentIndex()
        self.dbName = self.dbList[selectedIndex]
        self.HS.setDb(self.dbName)
        self.setDatabase()

    def compare(self):
        self.drawTable([[]])
        self.buttonCompare.hide()
        self.progressBar.show()
        self.buttonCompare.repaint()
        self.progressBar.repaint()
        inputSequence = self.sequenceInput.toPlainText()
        self.HS= HaplotypeSearcher(self.dbName)
        self.HS.signals.result.connect(self.showResults)
        tempFile = self.resourcePath("/tmp.fa")
        file = open(tempFile, "w+")
        file.write(inputSequence)
        file.close()
        self.numSeqs = self.resultLenghtSpin.value()
        self.HS.setQueryData("tmp.fa", self.numSeqs)
        self.HS.setOption("compare")
        self.threadPool.start(self.HS)
        self.HS.searchHaplotypes("tmp.fa", self.numSeqs)
        #results = [['DRB3*0201-DRB3*2704', 235.645, 1.57613e-65, 140, 147, 0.952], ['DRB3*1201-DRB3*2704', 239.338, 1.22034e-66, 143, 151, 0.947], ['DRB3*1201-DRB3*0201', 239.338, 1.22034e-66, 139, 147, 0.946], ['DRB3*0201-DRB3*0201', 239.338, 1.21842e-66, 139, 147, 0.946], ['DRB3*701-DRB3*0201', 228.258, 2.63927e-63, 139, 147, 0.946], ['DRB3*0201-DRB3*2708', 235.645, 1.57613e-65, 139, 147, 0.946], ['DRB3*0201-DRB3*2701', 235.645, 1.57613e-65, 139, 147, 0.946], ['DRB3*0201-DRB3*2710', 235.645, 1.57613e-65, 139, 147, 0.946], ['DRB3*1201-DRB3*1201', 241.185, 3.393e-67, 142, 151, 0.94], ['DRB3*701-DRB3*1201', 231.952, 2.04028e-64, 142, 151, 0.94]]

    def drawTable(self, data):
        #header = ["Combinacion", "Score", "E-value", "Similitud"]
        self.tablemodel = CustomTableModel(data)

        # Creating a QTableView
        self.tableResults.setModel(self.tablemodel)
        self.horizontal_header = self.tableResults.horizontalHeader()
        self.horizontal_header.resizeSections(QHeaderView.Stretch)
        self.horizontal_header.setStretchLastSection(True)

    def dbReady(self):
        self.setDatabases()
