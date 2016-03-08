[x1] =[int(i) for i in raw_input().split()]

def divisores(numero):
	divisores = []
	for x in range(numero):
		if x != 0:		
			if x1%x == 0:
				divisores.append(x)
	return divisores


def somaDivisores(divisores):
	soma = 0
	for x in divisores:
		soma += x
	return soma

if somaDivisores(divisores(x1)) == x1:
	print 'eh perfeito'
else:
	print 'nao eh perfeito'