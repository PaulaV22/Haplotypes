from PySide.QtCore import *
import os
from Model.HaplotypesSearcher import HaplotypesSearcher as HaplotypeSearcher


class DeleteController:

    def __init__(self, widAddDB):
        self.widget = widAddDB
        self.threadPool = QThreadPool()

    def configureDeleteView(self):
        self.selectedDbName=None
        self.widget.labelProcessDelete.hide()
        self.widget.askingWidgetDelete.hide()
        self.widget.buttonDelete.setEnabled(True)
        self.widget.buttonDelete.clicked.connect(self.showWidget)
        self.HS = HaplotypeSearcher()
        self.setDatabases()
        self.widget.progressBar_3.setMinimum(0)
        self.widget.progressBar_3.setMaximum(0)
        self.widget.progressBar_3.setVisible(False)
        self.projectPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.widget.buttonBox.accepted.connect(self.deleteDb)
        self.widget.buttonBox.rejected.connect(self.hideWidget)

    def removeItem(self):
        self.dbList = self.HS.getDatabases()
        index = self.widget.selectDeleteDatabase.findText(self.selectedDbName)
        self.widget.selectDeleteDatabase.removeItem(index)
        self.widget.selectDatabase.removeItem(index)

    def setDatabases(self):
        self.dbList = self.HS.getDatabases()
        for db in self.dbList:
            self.widget.selectDeleteDatabase.addItem(db)


    def showWidget(self):
        self.widget.labelProcessDelete.hide()
        selectedIndex = self.widget.selectDeleteDatabase.currentIndex()
        self.selectedDbName = self.dbList[selectedIndex]
        if (self.selectedDbName):
            self.widget.askingWidgetDelete.show()

    def hideWidget(self):
        self.widget.askingWidgetDelete.hide()

    def deleteDb(self):
        self.widget.labelProcessDelete.setText("Eliminando la base de datos")
        self.widget.labelProcessDelete.show()
        self.widget.progressBar_3.show()
        self.HS = HaplotypeSearcher(self.selectedDbName)
        self.HS.setNewDb(self.selectedDbName)
        self.HS.signals.deleted.connect(self.deletedDb)

        self.HS.setOption("deletedb")
        self.threadPool.start(self.HS)

    def deletedDb(self):
        self.hideWidget()
        self.removeItem()
        self.widget.labelProcessDelete.setText("La base de datos ha sido eliminada correctamente ")
        self.widget.progressBar_3.hide()

