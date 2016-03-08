import zipfile
import os
import re
import string

class Descompactador(object):

	def descompactarZips(self, arquivosCompactados, destino):
		for file in arquivosCompactados:
			#separa somente a matricula para criar uma pasta com os codigos fontes dentro
			dirAluno =  string.split(file, '_')
			dirAluno =  string.split(dirAluno[1], '.')[0]
			#print dirAluno
			#recebe um arquivo .zip
			_zip = zipfile.ZipFile(file)
			#print "Arquivos zipados em %s, %s"% (dirAluno , _zip.namelist())
			#extrai todos os arquivos contidos no zip
			#para uma pasta ex: lista/110066715/files.py
			_zip.extractall(destino+"/"+dirAluno)



