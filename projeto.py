from random import randint

def criarMatriz(numConvidados, listaDeAfinidades):
    matriz = [[0 for _ in range(numConvidados)] for _ in range(numConvidados)]
    
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
    instancia = instancia.readlines()
    numConvidados = 0
    matriz = []

    for i in range(len(instancia)):
        #print("linha " + str(i) + ": " + instancia[i])
        if (instancia[i] == "#quantidade_convidados\n"):
            numConvidados = int(instancia[i+1])
        if(instancia[i] == "#beneficios\n"):
            matriz = criarMatriz(numConvidados, instancia[i:len(instancia)])
    print(numConvidados)
    print()
    printMatriz(matriz)

#n = int(input('Quantos convidados? '))
# numMesas =  int(input('Quantas mesas? '))
# limMin =  int(input('Qual o mínimo de pessoas que devem sentar em cada mesa? '))
# limMax =  int(input('E qual o máximo? '))

#matriz = criarMatriz(n)
#printMatriz(matriz)
lerInstancia("instancias\/n20c5_A.txt")