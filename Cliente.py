import  ConfigParser

from app.br.unb.cic.corretor import Gabarito
from app.br.unb.cic.Facade import Facade
from app.br.unb.cic.util import ListarArquivos
from app.br.unb.cic.util import GerarCsv


cfg = ConfigParser.ConfigParser()
cfg.read('config.ini')


listasCompactadas = cfg.get('locais', 'listasCompactadas')
listasDescompactadas = cfg.get('locais', 'listasDescompactadas')
casosTeste = cfg.get('locais','casosTeste')
gabaritos = cfg.get('locais','gabaritos')
dirCSV = cfg.get('locais','csv')


#padrao para listar os arquivos .zip de um diretorio
#patternZip = re.compile('lista1_\d{9}.zip')
#subistituir por funcao

patternTeste = '\d{1,2}.txt'
patternTempTest = '\d{1,2}_\d{1,2}.txt'
patternReultados = '\d{2}.txt'
patternZip = 'lista1_\d{9}.zip'
patternPyFiles = '\d{1,9}.py'

#pattern Facade
facade = Facade()

#listar todos arquivos com os casos de teste existente
arquivoTestes = facade.listarAllFiles(patternTeste, [casosTeste])

#listar todos arquivos com as solucoes esperadas dos testes
arquivosSolucoesPropostas = facade.listarAllFiles(patternTeste, [gabaritos])

#lista todos os subdirs em um diretorio especifico
subDirInRoot = facade.listarAllSubdirs(listasCompactadas)

#lista todos os zips no subdiretorios encontrados
zipsInRoot = facade.listarAllFiles(patternZip, subDirInRoot)

try:
	#descompacta todos os zips encontrados em um destino
	#criando um diretorio com o numero da matricula para cada zip encontrado
	facade.descompactarZips(zipsInRoot, listasDescompactadas)
except UnZipError:
	print UnZipError


#lista todos os 
dirAlunos = facade.listarAllSubdirs(listasDescompactadas)
#para remover a raiz 
dirAlunos.pop(0)

#lista de alunos com todos os arquivos fontes dos alunos
alunos = facade.Alunos(patternPyFiles, dirAlunos)

#eh adicionado no dicionario que o aluno contem {questao:[respostasObtidas]} os valores
#dos testes realizados
alunosTestados = facade.testarCodigosAluno(alunos, arquivoTestes, casosTeste)

#lista os arquivos com as respostas e monta um dicionario contento
#{questao:[solucoes]}
gabarito = Gabarito(arquivosSolucoesPropostas)
dicionarioGabarito = gabarito.getDicionarioGabarito()

#executa a correcao dos codigos dos alunos comparando
#a resposta dos alunos com as propostas no gabarito
alunosCorrigidos = facade.Corrigir(alunosTestados, gabarito)


facade.gerarCsv(alunosTestados, gabarito, dirCSV)
