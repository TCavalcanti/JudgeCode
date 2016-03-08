import collections

#Classe aluno:
class Aluno(object):


	def __init__(self, matricula, diretorio, listaArquivos):
		self.__matricula = matricula
		self.__diretorio = diretorio
		self.__listaArquivos = listaArquivos
		self.__dicionarioInputs = {}
		self.__dicionarioRespostas = {}
		self.__dicionarioQuestoesCorrigidas = {}


		### --- SETS --- ###
	def setMatricula(self, matricula):
		self.__matricula = matricula

	def setDiretorio(self, diretorio):
		self.__diretorio = diretorio

	def setListaArquivos(self, listaArquivos):
		self.__listaArquivos = listaArquivos

	def addInputs(self, inputs):
		self.__dicionarioInputs.update(inputs)

	def addResposta(self, resposta):
		self.__dicionarioRespostas.update(resposta)

	def addQuestoesCorrigidas(self, questaoCorrigida):
		self.__dicionarioQuestoesCorrigidas.update(questaoCorrigida)		

		### --- GETS --- ###
	def getMatricula(self):
		return self.__matricula

	def getDiretorio(self):
		return self.__diretorio

	def getListArquivos(self):
		return self.__listaArquivos

	def getInputs(self):
		return collections.OrderedDict(sorted(self.__dicionarioInputs.items()))

	def getRespostas(self):
		return collections.OrderedDict(sorted(self.__dicionarioRespostas.items()))

	def getQuestoesCorrigidas(self):
		return collections.OrderedDict(sorted(self.__dicionarioQuestoesCorrigidas.items()))

	def getItemInput(self, key):
		return self.__dicionarioInputs[key]

	def getItemRespostaObtida(self, key):
		return self.__dicionarioRespostas[key]

	def getItemCorrigido(self, key):
		return self.__dicionarioQuestoesCorrigidas[key]