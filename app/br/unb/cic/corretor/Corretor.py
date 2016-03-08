#classe responsavel por comparar as respostas dos alunos com o gabarito proposto
import collections

from ..util.Aluno import Aluno
from Gabarito import Gabarito

class Corretor:

	def __init__(self, alunos, gabarito):
		self.__alunos = alunos
		self.__gabarito = gabarito
		self.__corrigir()



	def getAlunosCorrigidos(self):
		return self.__alunos


	#compara as repostas dos alunos com as contidas no gabarito e adiciona no dicionario
	# de questoes corrigidas do aluno
	def __corrigir(self):
		for aluno in self.__alunos:
			listaSolucoes = {}
			for exercicio, respostas in aluno.getRespostas().items():
				correcao = []
				for respostaAluno, gabarito in zip(respostas, self.__gabarito.getItem(exercicio)):
					if respostaAluno == gabarito:
						correcao.append('acertou')
					else:
						correcao.append('errou')
				listaSolucoes.update({exercicio:correcao})
			aluno.addQuestoesCorrigidas(collections.OrderedDict(sorted(listaSolucoes.items())))				


		return self.__alunos



