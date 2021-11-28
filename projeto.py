from random import randint

def criarMatriz():
    matriz = [[0 for _ in range(numConvidados)] for _ in range(numConvidados)]
    
    for l in range(numConvidados):
        for c in range(numConvidados):
            if(l < c):
                matriz[l][c] = randint(-9,9)
                matriz[c][l] = matriz[l][c]
                print(matriz[l][c], end="\t")                
            elif(l == c):
                matriz[l][c] = "-"
                print(matriz[l][c], end="\t")                
            else:
                print(" \t", end="")
            
        print()
        
numConvidados = int(input('Quantos convidados? '))
# numMesas =  int(input('Quantas mesas? '))
# limMin =  int(input('Qual o mínimo de pessoas que devem sentar em cada mesa? '))
# limMax =  int(input('E qual o máximo? '))

criarMatriz()