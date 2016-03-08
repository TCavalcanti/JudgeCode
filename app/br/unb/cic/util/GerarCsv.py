import csv

from ..corretor.Gabarito import Gabarito
from ..util.Aluno import Aluno

class GerarCsv:


	def gerarCsv(self, alunos, dicionarioGabarito, dirCsv):
		for aluno in alunos:
			f = open(dirCsv+aluno.getMatricula()+'.csv', 'w')
			csvAluno = csv.writer(f)
			virg =','
			#print "########### Solucoes Aluno:",aluno.getMatricula()
			exercicios = [x.split('/')[-1] for x in aluno.getListArquivos()]
			for exercicio in exercicios:
				csvAluno.writerow(["Questao", exercicio])

				inputs = ['Inputs']
				inputs += ((str(x) for x in aluno.getItemInput(exercicio)))

				respostasObtidas = ['Respostas Obtidas']
				respostasObtidas += (str(y) for y in aluno.getItemRespostaObtida(exercicio))
				
				gabaritoProposto = ['Gabarito Proposto']
				gabaritoProposto += (str(y) for y in dicionarioGabarito.getItem(exercicio))

				respostasCorrigidas = ['Respostas Corrigidas']
				respostasCorrigidas += (str(z) for z in aluno.getItemCorrigido(exercicio))

				csvAluno.writerow(inputs)
				csvAluno.writerow(respostasObtidas)
				csvAluno.writerow(gabaritoProposto)
				csvAluno.writerow(respostasCorrigidas)
				csvAluno.writerow([])
			f.close()