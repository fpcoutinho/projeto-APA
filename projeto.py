from random import randint

numConvidados = int(input('Quantos convidados? '))

matriz = [[0 for _ in range(numConvidados)] for _ in range(numConvidados)]
    
for l in range(numConvidados):
    for c in range(numConvidados):
        if(l < c):
            matriz[l][c] = randint(-9,9)
        elif(l == c):
            matriz[l][c] = "-"
        else:
            matriz[l][c] = " "
        print(matriz[l][c], end="\t")
        
    print()
