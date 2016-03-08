alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def codificar(key, string):
	codigo = []
	for char in string:
        #pegar o valor da posicao de char com o deslocamento (key + posicao) mod 26
		valor = ((-key+alfabeto.find(char))%26)
		codigo.append(alfabeto[valor])
	return codigo
 
    #Quantidade de caso de teste: 
    #[int(i) for i in raw_input().split()]
	#[k, code] = [for i in raw_input().split()]

inputs = raw_input().split()
	

k = int(inputs.pop(0))
string = inputs.pop(0)

print ''.join(codificar(k, string))