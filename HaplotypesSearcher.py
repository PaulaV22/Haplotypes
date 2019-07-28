import SimpleDbCreator as SC
import SimpleBlast as S
import AmbiguousDbCreator as AC
import GlobalBlast as GC
import ResultsAnalizer as RA
import os
import DbAdmin as DB

class HaplotypesSearcher:
    def __init__(self):
        self.db = "BoLa"
        self.simpleDbCreator = SC.SimpleDbCreator(self.db, "Blastdb", "secuencias", "fasta")
        self.globalBlast = GC.GlobalBlast("Blastdb", "secuencias", "salida", "fasta", "BlastResult", self.db)
        self.ambiguousDbCreator = AC.AmbiguousDbCreator("BlastResult", "Nuevadb" , "salida", "fasta", "DbAmbigua", self.db)
        self.simpleBlast = S.SimpleBlast("DbAmbigua", "salida", "salida", "fasta", "FinalResult", self.db)
        self.resultsAnalizer = RA.ResultsAnalizer("FinalResult",self.db)
        self.projectPath = os.path.dirname(os.path.abspath(__file__))
        self.dbAdmin = DB.DbAdmin()

    def searchHaplotypes(self):
        queryName= "queryTestBolaModifLarga.fa"
        queryPath = self.projectPath + "/" +queryName

        ######################### CONFIGURACION DE LA BASE DE DATOS ########################################
        ####crear la bd con los archivos originales de BoLa####
        self.simpleDbCreator.makeDb()
        ####alinear todas las secuencias de BoLa entre si generando un archivo de salida por cada alineacion (n x n)####
        #self.globalBlast.align(self.db)
        ####armar la base de datos con las posibles combinaciones (Nuevadb)####
        #self.ambiguousDbCreator.makeDb()
        ####self.ambiguousDbCreator.printAmbiguousPos()

        ######################### USO DE LA BASE DE DATOS CON UNA QUERY ########################################

        # alinear y obtener resultados de la query deseada
        #self.simpleBlast.align(queryPath, queryName)
        #self.resultsAnalizer.getSimilarSequences(6)
        print ("fin")

    def probarGlobalComparator(self):
        self.globalBlast.align("BoLa")

    def probarAmbiguousDbCreator(self):
        self.ambiguousDbCreator.makeDb()
        query = self.projectPath + '/BoLa/prueba.fa'
        self.simpleBlast.align(query, "prueba")

    def probarSimpleDbCreator(self):
        self.simpleDbCreator.makeDb()


    def deleteSequence(self, db, sequence):
        self.dbAdmin.deleteSequence(self.projectPath,db,sequence)

searcher = HaplotypesSearcher()
searcher.searchHaplotypes()
#searcher.deleteSequence("BoLa", "DRB3_0101.fa")
#searcher.probarGlobalComparator()
#searcher.probarSimpleDbCreator()
#searcher.probarAmbiguousDbCreator()
