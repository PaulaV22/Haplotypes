from __future__ import division
import os
from Bio import SearchIO
import json
class ResultsAnalizer:

    def __init__(self, resultsPath, dbName, categories, categoriesPath):
        # recibe (FinalResult, BoLa o Prueba2)
        self.resultsPath = resultsPath
        self.dbName = dbName
        self.resultFiles = resultsPath+"/"+dbName
        self.categories = categories
        self.categoriesPath = categoriesPath

    def mini(self, weight1, weight2):
        if (weight1>weight2):
            return weight2
        return weight1

    def getWeight(self, sequenceId, sequencesCategories, file):
        sequenceId.replace("_", "*", 1)
        seq1 = sequenceId.split('/')[0]
        seq2 = sequenceId.split('/')[1]
        seq1Id = seq1.replace("*", "_")
        seq2Id = seq2.replace("*", "_")
        if ("DRB3*902/DRB3*1103" in sequenceId):
            weight1 = sequencesCategories.get(seq1Id)
            weight2 = sequencesCategories.get(seq2Id)
            if (weight1 is None) and (weight2 is None):
                return 1
            if not (weight1 is None) and (weight2 is None):
                return self.categories.get(weight1)
            if not (weight2 is None) and (weight1 is None):
                return self.categories(weight2)
            if not (weight1 is None) and not (weight2 is None):
                return self.mini(self.categories.get(weight1), self.categories.get(weight2))
        else:
            weight1 = sequencesCategories.get(seq1Id)
            weight2 = sequencesCategories.get(seq2Id)
            if (weight1 is None) and (weight2 is None):
                return 1
            if not (weight1 is None) and (weight2 is None):
                return self.categories.get(weight1)
            if not (weight2 is None) and (weight1 is None):
                return self.categories(weight2)
            if not (weight1 is None) and not (weight2 is None):
                return self.mini(self.categories.get(weight1), self.categories.get(weight2))

    def getComplementary(self, id):
        seq1 = id.split('/')[0]
        seq2 = id.split('/')[1]
        output = seq2+"/"+seq1
        return output

    def getSimilarSequences(self, number=None):
        i = 0
        sequences = dict()
        categoriesFile = self.categoriesPath+"/"+self.dbName +".json"
        with open(categoriesFile, mode='r') as json_file:
            sequencesCategories = json.load(json_file)
        for bases, dirs, files in os.walk(self.resultFiles):
            for file in files:
                outputName = bases + "/" + file
                result = SearchIO.read(outputName, "blast-xml")
                for hits in result:
                    i = i+1
                    hsp = hits[0]
                    id = hsp.hit.id
                    score = hsp.bitscore
                    evalue = hsp.evalue
                    positives = hsp.pos_num
                    align_length = hsp.aln_span
                    percent = float("{0:.3f}".format(positives/align_length))
                    weight = self.getWeight(id,sequencesCategories, file)
                    complementary = self.getComplementary(id)
                    if not (complementary in sequences.keys()):
                        sequences[id] = [score * weight, evalue, positives, align_length, percent*weight]
        n = 0
        salida = []
        for key, value in sorted(sequences.items(), key=lambda item: item[1][4], reverse=True):
            if (number is None or n<number):
                value.insert(0, key)
                salida.append(value)
            n = n +1
        print(salida)
        return salida

