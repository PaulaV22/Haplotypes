import SimpleDbCreator as SC
import SimpleBlast as SB
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
import os
from Bio import SearchIO

# ESTA CLASE USA EL RESULTADO DE LA ALINEACION DE LAS SECUENCIAS HECHA POR SEARCHER. POR CADA COMPARACION GENERA UNA
# NUEVA SECUENCIA TENIENDO EN CUENTA QUE LAS DIFERENCIAS ENTRE LAS SECUENCIAS PUEDE SIGNIFICAR UN PUNTO POLIMORFICO
# EN LAS POSICIONES DONDE SE ENCUENTRAN DIFERENCIAS SE REEMPLAZAN POR LA LETRA QUE REPRESENTA ESA COMBINACION
# EN BASE A LAS SECUENCIAS GENERADAS SE CREA UN ARCHIVO DE SECUENCIAS NUEVO Y SE GENERA UNA NUEVA BASE DE DATOS DE
# LAS COMBINACIONES POSIBLES ENTRE LA SECUENCIA QUERY Y LAS PREEXISTENTES

# FALTA UNA CLASE SUPERIOR QUE LLAME A ESTA CLASE CON CADA SECUENCIA DE LA BD -->GLOBALSEARCHER  ???
# ESTA DEBERIA GENERAR O AGREGAR SI ES QUE EXISTE EL ARCHIVO DE SECUENCIAS RESUMIDOS
# UNA VEZ COMPARADAS TODAS LAS SECUENCIAS ENTRE SI LLAMAR A SIMPLEDBCREATOR QUE GENERE LAS BD BLAST EN BASE A LOS
# ARCHIVOS GENERADOS POR ESTA CLASE


class AmbiguousDbCreator:

    def __init__(self, filesPath, intermediateDb, outputFile, outputFormat, newDb, dbName):
        # recibe (BlastResult, Nuevadb, salida, fasta, "DbAmbigua", "BoLa")
        self.filesPath = filesPath +"/" + dbName
        self.intermediateDb = intermediateDb
        self.outputFile = outputFile
        self.outputFormat =outputFormat
        self.newDb = newDb
        self.dbName= dbName
        self.projectPath = os.path.dirname(os.path.abspath(__file__))
        self.sc = SC.SimpleDbCreator(intermediateDb, newDb, outputFile, outputFormat)
        self.ambiguousPos= dict()
        # super(AmbiguousDbCreator, self).__init__(dbPath, newDb, outputFile, outputFormat)

    def getNitrogenBase(self, q, h, i, queryid, hitid):
        if q == h:
            return q
        else:
            if (q == "A" and h == "G") or (q == "G" and h == "A"):
                self.ambiguousPos[str(i)+"_"+queryid+hitid] = "R"
                return "R"
            if (q == "C" and h == "T") or (q == "T" and h == "C"):
                self.ambiguousPos[str(i)+"_"+queryid+hitid] = "Y"
                return "Y"
            if (q == "C" and h == "G") or (q == "G" and h == "C"):
                self.ambiguousPos[str(i)+"_"+queryid+hitid] = "S"
                return "S"
            if (q == "A" and h == "T") or (q == "T" and h == "A"):
                self.ambiguousPos[str(i)+"_"+queryid+hitid] = "W"
                return "W"
            if (q == "A" and h == "C") or (q == "C" and h == "A"):
                self.ambiguousPos[str(i)+"_"+queryid+hitid] = "M"
                return "M"
            if (q == "T" and h == "G") or (q == "G" and h == "T"):
                self.ambiguousPos[str(i)+"_"+queryid+hitid] = "K"
                return "K"
            # faltan los casos de los guiones
            else:
                return "N"

    def getSequencesFromBlastResult(self, blastResult):
        sequences = []
        #print (len(blastResult))
        for hits in blastResult:
            hsp = hits[0]
            query = hsp.query
            hit = hsp.hit
            querySeq = query.seq
            hitSeq = hit.seq
            newSeq = Seq("", IUPAC.ambiguous_dna)
            for i, (q, h) in enumerate(zip(querySeq, hitSeq)):
            #for q, h in zip(querySeq, hitSeq):
                nitrogenBase = self.getNitrogenBase(q, h, i, query.id, hit.id)
                append = Seq(nitrogenBase, IUPAC.ambiguous_dna)
                newSeq = newSeq + append
            newSeqId = query.id + "/" + hit.id
            newSeqDescription = query.description + "_" + hit.description
            record = SeqRecord(newSeq, id=newSeqId, description=newSeqDescription)
            sequences.append(record)
        return sequences

    def makeDb(self):
        #self.sc.createFolder(self.intermediateDb)
        for bases, dirs, files in os.walk(self.filesPath):
            #SI NO CREA BIEN LA BBDD AMBIGUA VER DE DESCOMENTAR ESTO QUE CREABA UNA CARPETA DEMAS SIN USO PARA LA PRUEBA
            # newFolderPath = self.newDb + "/" + bases
            #self.sc.createFolder(newFolderPath)
            #print ("crea el directorio  " + newFolderPath)
            for file in files:
               # print(file)
                # por cada archivo de salida que se haya generado en la busqueda,
                # generar una nueva secuencia fasta por cada uno de los resultados obtenidos
                outputName = self.projectPath + "/"  + bases + "/" + file
                blast_qresult = SearchIO.read(outputName, "blast-xml")
                sequences = self.getSequencesFromBlastResult(blast_qresult)
                sequencePath = self.newDb + "/" + self.dbName +"/" + file
                self.sc.createFolder(sequencePath)
                self.sc.saveSequencesInFile(sequencePath, sequences, file)
                db = sequencePath
                self.sc.setOutputFile(file)
               #para evitar que se genere mal alguna base de datos y el error aparezca en etapas posteriores
                while(self.testFails(db, file)):
                    self.sc.makeBlastDb(db)


    def getAmbiguousPos(self):
        return self.ambiguousPos

    def printAmbiguousPos(self):
        print(self.ambiguousPos)


    def testFails(self,db, file):
        print("A TESTEAR DB "+db)
        if (len([f for f in os.listdir(db)]) <7):
            return True
        outputPath = "Test"+"/"+self.dbName+"/"+file
        sb = SB.SimpleBlast(db, "salida", "salida", "fasta", outputPath)
        queryName = "queryTestBola.fa"
        queryPath = self.projectPath + "/" + queryName
        try:
            sb.align(queryPath, queryName)
        except:
            return True
        return False