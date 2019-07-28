from __future__ import division
import os
from Bio import SearchIO

class ResultsAnalizer:

    def __init__(self, resultsPath, dbName):
        # recibe (FinalResult, BoLa o Prueba2)
        self.resultsPath = resultsPath
        self.dbName = dbName
        self.resultFiles = resultsPath+"/"+dbName

    def getSimilarSequences(self, number=None):
        i = 0
        sequences = dict()
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
                    sequences[id] = [score, evalue, positives, align_length, percent]
        n = 0
        salida = []
        for key, value in sorted(sequences.items(), key=lambda item: item[1][4], reverse=True):
            if (number is None or n<number):
                value.insert(0, key)
                salida.append(value)
            n = n +1
        print(salida)
        return salida

