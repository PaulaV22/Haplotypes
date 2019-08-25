import SimpleDbCreator as SC
import SimpleBlast as S
import AmbiguousDbCreator as AC
import GlobalBlast as GC
import ResultsAnalizer as RA
import os
import DbAdmin as DB
import shutil
import json

class HaplotypesSearcher:
    def __init__(self):
        self.db = "BoLa"
        self.simpleDbCreator = SC.SimpleDbCreator(self.db, "Blastdb", "secuencias", "fasta")
        self.globalBlast = GC.GlobalBlast("Blastdb", "secuencias", "salida", "fasta", "BlastResult", self.db)
        self.ambiguousDbCreator = AC.AmbiguousDbCreator("BlastResult", "Nuevadb" , "salida", "fasta", "DbAmbigua", self.db)
        self.simpleBlast = S.SimpleBlast("DbAmbigua", "salida", "salida", "fasta", "FinalResult", self.db)
        self.categories  = {"ALTA": 1, "MEDIA": 0.7, "BAJA": 0.3}
        self.projectPath = os.path.dirname(os.path.abspath(__file__))
        self.categoriesPath = self.projectPath+"/Categories"
        self.resultsAnalizer = RA.ResultsAnalizer("FinalResult",self.db, self.categories,self.categoriesPath)
        if not os.path.exists(self.categoriesPath):
            os.makedirs(self.categoriesPath)
        #self.dbAdmin = DB.DbAdmin()

    def searchHaplotypes(self):
        queryName= "Muestra5.fa"
        queryPath = self.projectPath + "/" +queryName

        # alinear y obtener resultados de la query deseada
        self.simpleBlast.align(queryPath, queryName)
        self.resultsAnalizer.getSimilarSequences(10)
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

    def congifureDb(self, db):
        ####crear la bd con los archivos originales de BoLa####
        self.simpleDbCreator.makeDb()
        ####alinear todas las secuencias de BoLa entre si generando un archivo de salida por cada alineacion (n x n)####
        self.globalBlast.align(self.db)
        ####armar la base de datos con las posibles combinaciones (Nuevadb)####
        self.ambiguousDbCreator.makeDb()
        categories = {}
        categoriesFile = self.projectPath + "/Categories/" + db + ".json"
        with open(categoriesFile, mode='w+') as f:
            json.dump(categories, f)
        #####GUARDARLO EN ACHIVO JSON

    def restartDb(self,db):
        BlastDb = self.projectPath + '/BlastDb/' + db
        BlastResult = self.projectPath + '/BlastResult/' + db
        DbAmbigua = self.projectPath + '/DbAmbigua/' + db
        FinalResult = self.projectPath + '/FinalResult/' + db
        try:
            shutil.rmtree(BlastDb)
        except:
            pass
        try:
            shutil.rmtree(BlastResult)
        except:
            pass
        try:
            shutil.rmtree(DbAmbigua)
        except:
            pass
        try:
            shutil.rmtree(FinalResult)
        except:
            pass
        try:
            os.remove(self.projectPath+"/Categories/"+db+".json")
        except:
            pass
        self.congifureDb(db)

    def deleteSeq(self, db, seqPath):
        try:
            os.remove(seqPath)
            self.restartDb(db)
        except:
            print("La carpeta no existe")
        self.congifureDb()


    def addSeq(self, path,db, name, seq):
        file = open(path+"/"+name+".fa", "w")
        file.write(">"+name + os.linesep)
        file.write(seq)
        file.close()
        self.restartDb(db)

    def setCategoryToFilesInDb(self, db, folder, category):
        folderPath = self.projectPath +"/"+db+"/"+folder
        categoriesFile = self.projectPath+ "/Categories/"+db+".json"
        with open(categoriesFile, mode='r') as json_file:
            data = json.load(json_file)
        for bases, dirs, files in os.walk(folderPath):
            for file in files:
                #newJson = '{"'+os.path.basename(file.name)+'" : "'+self.categories[category]+'"}'
                data[file[:-3]] = category
        with open(categoriesFile, 'w') as f:  # writing JSON object
            json.dump(data, f)


####self.ambiguousDbCreator.printAmbiguousPos()
searcher = HaplotypesSearcher()
#searcher.restartDb("BoLa")
#searcher.setCategoryToFilesInDb('BoLa', 'Mas_frecuentes', "ALTA")
searcher.searchHaplotypes()

#searcher.congifureDb()
#searcher.deleteSequence("BoLa", "DERB3_4501.fa")
#
#searcher.deleteSeq("BoLa","C:\Users\Paula\PycharmProjects\Haplotypes\BoLa\Mas_frecuentes\DRB3_2705.fa")
#searcher.addSeq("C:\Users\Paula\PycharmProjects\Haplotypes\BoLa\Mas_frecuentes","BoLa", "DRB3_2705",
                          #"GGAGTATTATAAGAGAGAGTGTCATTTCTTCAACGGGACCGAGCGGGTGCGGTTCCTGGACAGATGCTACACTAATGGAGAAGAGACCGTGCGCTTCGACAGCGACTGGGGCGAGTTCCGGGCGGTGACCGAGCTAGGGCGGCCGGACGCCGAGTACTGGAACAGCCAGAAGGACTTCCTGGAGGAGAGGCGGGCCGCGGTGGACAGGGTGTGCAGACACAACTACGGGGTCGTGGAGAGTTTCACTGTG")
#searcher.probarGlobalComparator()
#searcher.probarSimpleDbCreator()
#searcher.probarAmbiguousDbCreator()

