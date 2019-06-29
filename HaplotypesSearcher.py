import SimpleDbCreator as SC
import SimpleBlast as S
import AmbiguousDbCreator as AC
import GlobalBlast as GC
import os


class HaplotypesSearcher:
    def __init__(self):
        self.simpleDbCreator = SC.SimpleDbCreator("Prueba2", "Blastdb", "secuencias", "fasta")
        self.globalBlast = GC.GlobalBlast("Blastdb", "secuencias", "salida", "fasta", "BlastResult")
        self.ambiguousDbCreator = AC.AmbiguousDbCreator("BlastResult", "Nuevadb" , "salida", "fasta", "DbAmbigua")
        self.simpleBlast = S.SimpleBlast("DbAmbigua", "salida", "salida", "fasta", "FinalResult")
        self.projectPath = os.path.dirname(os.path.abspath(__file__))

    def searchHaplotypes(self):
        print ("empieza main")
        query = self.projectPath + '\queryTest.fa'
        #crear la bd con los archivos originales de BoLa
        #self.simpleDbCreator.makeDb()
        # alinear todas las secuencias de BoLa entre si generando un archivo de salida por cada alineacion (n x n)
        #self.globalBlast.align("Prueba2")
        # armar la base de datos con las posibles combinaciones (Nuevadb)
        # self.ambiguousDbCreator.makeDb()
        # self.ambiguousDbCreator.printAmbiguousPos()
        # alinear y obtener resultados de la query deseada
        self.simpleBlast.align(query, "queryTest")
        print ("fin")

    def probarGlobalComparator(self):
        self.globalBlast.align("BoLa")

    def probarAmbiguousDbCreator(self):
        self.ambiguousDbCreator.makeDb()
        query = self.projectPath + '/BoLa/prueba.fa'
        self.simpleBlast.align(query, "prueba")

    def probarSimpleDbCreator(self):
        self.simpleDbCreator.makeDb()

searcher = HaplotypesSearcher()
searcher.searchHaplotypes()
#searcher.probarGlobalComparator()
#searcher.probarSimpleDbCreator()
#searcher.probarAmbiguousDbCreator()
