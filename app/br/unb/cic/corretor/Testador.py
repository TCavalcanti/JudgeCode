import commands

from ..timeout.Timeout import Timeout

#Classe responsavel por testar os programas dos alunos
class Testador:

	#construtor defult instanciando o objeto Timeout
	def __init__(self):
		self.__timeout = Timeout()
		self.__dicionarioInputs = ()


	def run(self, arquivoFonte, arquivoTeste):
		try:
			file = open(arquivoTeste, 'r')
			self.__dicionarioInputs = ()
			inputs = []
			result = []	

			lines = file.readlines()

			for line in lines:
				#captura cada linha de cada arquivo de teste removendo o \n comum no fim de cada linha
				INPUT = line.split('\n')[0]

				#adiconar o input para o diconario de Inputs
				inputs.append(INPUT)

				#monta o comando para executaro codigo do aluno com cada entrada no arquivo teste
				comando = 'INPUT="'+INPUT+'" && echo $INPUT | python ' + arquivoFonte

				testarComTimeout = self.__timeout.timeout(commands.getoutput, {comando})
				#result.append(commands.getoutput(comando))
				result.append(testarComTimeout)

			file.close()
		except IOError:
			result.append('Can\'t open test case: '+arquivoTeste)

		self.__dicionarioInputs = ({arquivoFonte.split('/')[-1]: inputs})
		
		#retorna o resultado obtido no teste
		return result

	#metodo para testar os codigo do aluno
	def testarCodigosAluno(self, alunos, arquivosTestes, pastaCasosDeTeste):
		for aluno in alunos:
			for arquivoFonteAluno in aluno.getListArquivos():
				#pega o nome do arquivo fonte do aluno e substitui o .py por .txt que ser o teste equivalente
				nomeArquivoFonte = arquivoFonteAluno.split('/')[-1]
				
				#----------------------------------------------substitiu o .py por .txt do arquivo de teste equivalente
				arquivoTesteEquivalente = pastaCasosDeTeste+nomeArquivoFonte.replace('.py', '.txt')
			
				#se o arquivo teste existir eh executado o teste no arquivo fonte do aluno
				if arquivoTesteEquivalente in arquivosTestes:
					#executa o teste no aruqivo
					respostasQuestao = self.run(arquivoFonteAluno, arquivoTesteEquivalente)
					
					#armazena o resultado do teste em um dicionario contido obj aluno
					dicionarioResposta = ({nomeArquivoFonte: respostasQuestao})

				#caso nao exista arquivo teste equivalente eh armazenado no dicionario
				else:
					dicionarioResposta = ({nomeArquivoFonte: ['arquivo sem teste']})

				#adicoina as respostas obtidas pelos alunos no testes
				aluno.addResposta(dicionarioResposta)
				aluno.addInputs(self.__dicionarioInputs)

		#retorna os alunos
		return alunos
