[x1, x2, x3] =[int(i) for i in raw_input().split()]

def bubleSort(lista):
	if len(lista) <= 1:
		order = lista
	else:
		for i in  range(0, len(lista)):
			for j in range(0, len(lista)-1):
				if lista[j] > lista[j+1]:
					aux = lista[j+1]
					lista[j+1] = lista[j]
					lista[j] = aux
		order = lista
		
	return str(order).strip('[]')


print bubleSort([x1, x2, x3])