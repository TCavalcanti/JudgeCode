import sys

from util.Descompactador import Descompactador
from util.ListarArquivos import ListarArquivos
from util.Aluno import Aluno
from corretor.Testador import Testador
from corretor.Corretor import Corretor
from util.GerarCsv import GerarCsv

#Facade para simplificar o projeto
class Facade:

	def __init__(self):
		self.__listarArquivos = ListarArquivos()
		self.__descompactador = Descompactador()

	def listarAllSubdirs(self, baseDir):
		return self.__listarArquivos.listarAllSubdirs(baseDir)

	def listarAllFiles(self, pattern, dirs):
		return self.__listarArquivos.listarAllFiles(pattern, dirs)

	def descompactarZips(self, arquivosCompactados, destino):
		try:
			self.__descompactador.descompactarZips(arquivosCompactados, destino)
		except:
			raise UnZipError("Erro no descompactador")


	def Alunos(self, pattern, dirAlunos):
		alunos = []
		for dirAluno in dirAlunos:
			matricula = dirAluno.split('/')
			matricula =  matricula[1]
	
			arquivos = self.listarAllFiles(pattern, [dirAluno])
			alunos.append(Aluno(matricula, dirAluno, arquivos))
		return alunos



	def createTempTestFile(self, tempFolder, arquivoTeste):
		self.tempFileTest.createTempTestFile(tempFolder, arquivoTeste)

	def removeTempFile(self, tempFolder):
		self.tempFileTest.removeTempFile(tempFolder)


	#retorna uma lista com os testes realizados no arquivo
	#def run(self, arquivoFonte, arquivoTeste):
	#	testador = Testador()
	#	return testador.run(arquivoFonte, arquivoTeste)

	def testarCodigosAluno(self, alunos, arquivosTestes, pastaCasosDeTeste):
		testador = Testador()
		alunosTestados = testador.testarCodigosAluno(alunos ,arquivosTestes, pastaCasosDeTeste)
		return alunosTestados


	#adicona um dicionario contendo as questoes corrigidas do aluno
	def Corrigir(self , alunos, gabarito):
		corretor = Corretor(alunos, gabarito)
		return corretor.getAlunosCorrigidos


	def gerarCsv(self, alunosCorrigidos, gabarito, dirCSV):
		gerarCsv = GerarCsv()
		gerarCsv.gerarCsv(alunosCorrigidos, gabarito, dirCSV)
