if __name__ == '__main__':
    [x, y] =[int(i) for i in raw_input().split()]
 
    if x > y:
        maior = x
        menor = y
    else:
        menor = x
        maior = y
     
    lista = [k for k in range(menor, maior)]
    lista.append(maior)
 
    soma = 0
     
    for x in lista:
        if x%13 != 0 :
            soma+=x
 
    print "%d" % soma