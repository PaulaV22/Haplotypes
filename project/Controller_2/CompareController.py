
import numpy as np
from project.model import HaplotypesSearcher as HaplotypeSearcher
from project.model.HaplotypesSearcher import HaplotypesSearcher
import os
import sys

class CompareController():

    def __init__(self):
        self.HS = HaplotypesSearcher()
        self.dbList = self.getDatabases()
        self.dbName = self.HS.getDatabases()[0]

    def resourcePath(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        output = base_path + relative_path
        return output

    def getDatabases(self):
        output = []
        dbs= self.resourcePath("/Databases")
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

    def compare(self, sequence, numResults, database):
        if not self.HS:
            self.HS = HaplotypeSearcher()
        self.HS.setDb(database)
        tempFile = self.resourcePath("/tmp.fa")
        file = open(tempFile, "w+")
        file.write(sequence)
        file.close()
        print(numResults)
        results = self.HS.getResults("tmp.fa",numResults)
        return results

    def showResults(self, results):
        dt = np.dtype('string', 'float', 'int')
        resultsArray = np.array(results, dtype=dt)
        return resultsArray
        # self.drawTable(results)


