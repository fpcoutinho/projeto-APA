from random import randint

def criarMatriz(numConvidados):
    matriz = [["-" for _ in range(numConvidados)] for _ in range(numConvidados)]
    
    for l in range(numConvidados):
        for c in range(numConvidados):
            if(l < c):
                matriz[l][c] = randint(-9,9)
    return matriz

def printMatriz(matriz):
    for l in range(len(matriz)):
        for c in range(len(matriz)):
            if (l <= c):
                print(matriz[l][c], end="\t")
            else:
                print(" \t", end="")
        print()

def lerInstancia(arquivo):
    instancia = open(arquivo, 'r')
    for l in instancia:
        print(l)


n = int(input('Quantos convidados? '))
# numMesas =  int(input('Quantas mesas? '))
# limMin =  int(input('Qual o mínimo de pessoas que devem sentar em cada mesa? '))
# limMax =  int(input('E qual o máximo? '))

matriz = criarMatriz(n)
printMatriz(matriz)
