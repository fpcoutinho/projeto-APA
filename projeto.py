from random import randint

numConvidados = int(input("Quantos Convidados?\n"))

matrix = []
for l in range(numConvidados):
    for c in range(numConvidados):
	    matrix.append(randint(-9,9))
 
print(matrix)