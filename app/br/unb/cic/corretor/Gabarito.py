import collections

#Classe responsvel por gerar o dicionario dos gabaritos 
class Gabarito:

	#lista contendo o path dos arquivos com a solucao
	#lista contendo os alunos com suas respectivas respostas ja computadas
	def __init__(self, arquivosSolucao):
		self.__gabarito = {}
		#dicionario contendo todos os gabaritos propostos
		self.setGabarito(arquivosSolucao)
		

	def setGabarito(self, arquivosSolucao):

		for arquivoSolucao in arquivosSolucao:
			try:
				file = open(arquivoSolucao, 'r')
				#pega o nome do arquivo fonte da solucao e substitui .txt por .py para indicar a qual teste pertence
				nomeArquivoFonte = arquivoSolucao.split('/')[-1]
				#--------------------substitiu o .txt por .py para indicar a solucao do arquivo
				nomeSolucaoArquivo = nomeArquivoFonte.replace('.txt', '.py')

				solucoes = []

				lines = file.readlines()
				for line in lines:
					#adiconar cada linha a seu dicionario
					solucoes.append(line.split('\n')[0])

				file.close()

				#armazena o resultado do teste em um dicionario
				dicionarioSolucoes = ({nomeSolucaoArquivo: solucoes})
				self.__gabarito.update(dicionarioSolucoes)
				
			except IOError:
				print 'Can\'t open test case: '+arquivoSolucao


	def getDicionarioGabarito(self):
		dic = collections.OrderedDict(sorted(self.__gabarito.items()))
		return dic


	def getItem(self, key):
		return self.__gabarito[key]

	


