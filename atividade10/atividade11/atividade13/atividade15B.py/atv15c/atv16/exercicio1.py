'''
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
'''

lista_valores = []
soma=0
multiplicação=1

for n in range(5):
    v = int(input("Digite 5 números:"))
    lista_valores.append(v)
    print(lista_valores)
    soma+=v
    multiplicação=multiplicação*v
# resultado = sum(v)

print("a soma dos números é:", soma)
print("a multiplicação dos números é:", multiplicação)