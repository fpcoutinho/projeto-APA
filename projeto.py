from random import randint

def criarMatriz():
    matriz = [["-" for _ in range(numConvidados)] for _ in range(numConvidados)]
    for lin in range(numConvidados):
        for col in range(numConvidados):
            if(lin < col):
                matriz[lin][col] = randint(-9,9)
            print(matriz[lin][col], end="\t")          
        print()
  
    print(matriz)


numConvidados = int(input('Quantos convidados? '))
criarMatriz()

# numMesas = int(input('Quantas mesas? '))
# limMin = int(input('Minimo por mesa: '))
# limMax = int(input('Maximo por mesa: '))

# mesas = [[limMin for _ in range(limMax)] for _ in range(numMesas)]
    

