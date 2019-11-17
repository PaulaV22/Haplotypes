import sys
import os
from PySide.QtGui import *
from PySide.QtCore import *
from View.compareView_ui import Ui_mainWindow
import numpy as np
from Model import *
from Model.HaplotypesSearcher import HaplotypesSearcher as HaplotypeSearcher

class Controller():
    def __init__(self, window):
        self.window = window
        self.projectPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.HS = HaplotypeSearcher()
        self.dbList = self.getDatabases()
        self.dbName =""

    def getProjectPath(self):
        return self.projectPath

    def getDatabases(self):
        output = []
        dbs= self.projectPath+"/Databases"
        for dir in os.listdir(dbs):
            output.append(dir)
        output.sort()
        return output


    def getDb(self):
        self.dbList = self.getDatabases()
        selectedIndex = self.window.selectDatabase.currentIndex()
        dbName = self.dbList[selectedIndex]
        return dbName


    def setDb(self, dbName):
        self.dbName= dbName
        self.HS.setDb(dbName)
