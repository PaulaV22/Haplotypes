import os
from Bio.Blast.Applications import NcbiblastnCommandline


# ESTA CLASE HACE LA BUSQUEDA EN LA BASE DE DATOS PARA UNA DETERMINADA SECUENCIA GENERANDO UNA SALIDA BLASTQRESULT.
# PARA ESO RECIBE:
#       1: EL PATH DONDE ESTA LA BASE DE DATOS BLAST
#       2: DBNAME ES EL NOMBRE DEL ARCHIVO DE SECUENCIAS RESUMIDO QUE SE GENERA CON SIMPLEDBCREATOR
#       3: OUTPUTNAME ES EL NOMBRE DEL ARCHIVO DE SALIDA QUE GENERARA EL COMANDO NCBIBLASTCOMMANDLINE (RESULTADOS)
#       4: OUTPUTFORMAT ES FASTA (FORMATO DEL ARCHIVO DE SECUENCIAS RESUMIDO)

class SimpleBlast:
    def __init__(self, dbPath, dbName, outputName, outputFormat, outputPath):
        self.dbPath = dbPath
        self.dbName = dbName
        self.outputName = outputName
        self.outputFormat = outputFormat
        self.outputPath = outputPath
        self.projectPath = os.path.dirname(os.path.abspath(__file__))


    def createFolder(self, newFolder):
        if not os.path.exists(newFolder):
            os.makedirs(newFolder)


    def align(self, query, queryName):
        self.createFolder(self.outputPath)
        #print ("query es " + query)
        i=0
        for bases, dirs, files in os.walk(self.dbPath):
            for file in files:
                # fileName es "secuencias.fasta" o salida.fasta
                fileName = self.dbName + "." + self.outputFormat
                if file[-5:] == self.outputFormat:
                    self.dbName = file[:-6]
                    # ahora tengo que armar un archivo de salida para cada una de las bases de datos
                    dbPath = self.projectPath + '/' + bases + '/' + self.dbName
                    output = self.projectPath + '/' + self.outputPath+ '/'+queryName+str(i)
                    #print(output + "   " + dbPath)
                    # ya se tiene la base de datos creada. Crear el comando para buscar la secuencia query en la bd y generar salida
                    blastnCline = NcbiblastnCommandline(query=query, db=dbPath, evalue=0.001, outfmt=5, out=output)
                    #print (blastnCline)
                    stdout, stderr = blastnCline()
                    i=i+1
