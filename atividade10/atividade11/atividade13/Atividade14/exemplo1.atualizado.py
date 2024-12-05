'''
1)escrever um algoritmo que leia 5 valores um de cada vez
2)contar quantos desses valores são negativos
3)escrever quantos valores são negativos
'''

contador = 1
contador_negativo = 0

while contador <=5:
    valor = int(input("Digite um valor:"))
    contador +=1
    if valor < 0:
        contador_negativo +=1

print("O total de números negativos foi:", contador_negativo)