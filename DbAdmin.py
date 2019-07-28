import os
from Bio import SeqIO
from Bio import SearchIO
import shutil

class DbAdmin:

    def deleteSequence(self, projectPath, db, file):
        self.deleteFromFolder(projectPath,db,file)
        self.deleteFromDb(projectPath,db,file, "BlastDb")
        #self.deleteFromAlignResult(projectPath,db,file,"BlastResult")
        #self.deleteFromDb(projectPath, db, file, "DbAmbigua")

    def contains(self, string1, string2):
        return string2 in string1

    # Borrarlo de la carpeta contenedora
    def deleteFromFolder(self,projectPath, db, file):
        dbPath = projectPath+"/"+db
        for bases, dirs, files in os.walk(dbPath):
            for f in files:
                if f == file:
                    try:
                        os.remove(dbPath+"/"+f)
                    except Exception as e:
                        print e

    # Borrarlo de la base de datos BlastDb o AmbiguousDb
    def deleteFromDb(self,projectPath, db,file, dbType ):
        dbPath = projectPath + "/" + dbType+"/" + db
        for bases, dirs, files in os.walk(dbPath):
            if len(dirs)>0:
                for d in dirs:
                    if self.contains(d,file[:-3]):
                        shutil.rmtree(dbPath+"/"+d)
                    else:
                        for f in os.listdir(dbPath+"/"+d):
                            if self.contains(f,"fasta"):
                                filePath = dbPath + "/" +d+"/"+ f
                                with open(filePath) as originalFasta, open(dbPath +"/"+d+ "/output.fasta", 'w') as correctedFasta:
                                    for seq_record in SeqIO.parse(originalFasta, "fasta"):
                                        if not(self.contains(seq_record.id,file[:-3])):
                                            SeqIO.write(seq_record, correctedFasta, 'fasta')
                                os.remove(filePath)
                                try:
                                    os.rename(dbPath + "/"+d+"/output.fasta", filePath)
                                except Exception as e:
                                    print(e)
            else:
                for f in os.listdir(dbPath):
                    if self.contains(f, "fasta"):
                        filePath = dbPath+ "/" + f
                        with open(filePath) as originalFasta, open(dbPath + "/" +"/output.fasta",
                                                                   'w') as correctedFasta:
                            for seq_record in SeqIO.parse(originalFasta, "fasta"):
                                if not (self.contains(seq_record.id, file[:-3])):
                                    SeqIO.write(seq_record, correctedFasta, 'fasta')
                        os.remove(filePath)
                        try:
                            os.rename(dbPath + "/" + "/output.fasta", filePath)
                        except Exception as e:
                            print(e)


    # Borrarlo de la base de datos ambigua BlastResult
    def deleteFromAlignResult(self, projectPath, db, file, alignResult):
        blastResultPath = projectPath + "/" + alignResult + "/" + db
        for bases, dirs, files in os.walk(blastResultPath):
            for f in files:
                filePath = blastResultPath + "/" + f

                # si el nombre del archivo a leer contiene el nombre del archivo a borrar, borrarlo
                if (self.contains(f, file[:-3])):
                    os.remove(filePath)
                # sino puede estar adentro la alineacion
                else:
                    with open(filePath) as originalXml:
                        result = SearchIO.read(originalXml, "blast-xml")
                        i = 0
                        for hits in result:
                            hsp = hits[0]
                            id = hsp.hit.id
                            if (id == file[:-3]):
                                result.hit_keys.pop(i)
                                result.hits.pop(i)
                                result.hsps.pop(i)
                                result.pop(i)
                            i = i + 1
                    os.remove(filePath)
                    SearchIO.write(result, filePath, 'blast-xml')