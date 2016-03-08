import re
if __name__ == "__main__":

	inputs = raw_input().split()
	cpf = inputs.pop(0)

	#RegEx responsavel por analisar o formato do CPF
	cpfPadrao = re.compile('[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}')
	def validaCpf(cpf):
		if cpfPadrao.match(cpf):
			return True
		else:
			return False


	#Funcao para calcular o digito 1
	def calcularD1(cpf):	
		d1 = 0
		for i in range(9):
			d1+=cpfToInteger[i]*(10-i)
			#print cpfToInteger[i], "*", (10-i)
	
		resto = d1%11
		if resto < 2:
			return 0
		else:
			return (11-resto)


	#Funcao para calcular o digito 2
	def calcularD2(cpf, d1):
		d2 = 0
		for i in range(9):
			#print 8-i,"-", 11-i
			d2+=cpfToInteger[i]*(11-i)
			#print cpfToInteger[8-i], "*", (11-i)
		d2+=d1*2

		resto = d2%11
		if resto < 2:
			return 0
		else:
			return (11-resto)


	if validaCpf(cpf):
		#transformar o cpf em uma lisa somente de numeros
		cpfToInteger = [int(x) for x in cpf if x != "." and x != "-" ]

		#copiar os nove primeiros digitos do cpf para uma lista
		cpfNumbers = cpfToInteger[:9]

		d1 = calcularD1(cpfNumbers)
		d2 = calcularD2(cpfNumbers, d1)

		if d1 == int(cpf[12]) and d2 == int(cpf[13]):
			print "CPF valido"
		else:
			print "CPF invalido"

	else:
		print "CPF invalido"

