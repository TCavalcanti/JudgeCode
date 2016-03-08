import os, re


class ListarArquivos:

	#metodo para listar todos os arquivos em um diretorio
	#varre o diretorio de forma recursiva pesquisando nos subdir's
	def listarAllSubdirs(self, root):
		allSubdirs = []
		for x in os.walk(root):
			#print x[0]
			allSubdirs.append(x[0]+'/')

		return allSubdirs

	
	#retorna uma lista de arquivos filtrada por um pattern pre-definido por exp.regular
	def listarAllFiles(self, pattern, dirs):
		pattern = re.compile(pattern)
		files = []
		for dir in dirs:
			for f in os.listdir(dir):
				if pattern.match(f):
					files.append(dir+f)
		sorted(files)
		return files

	



