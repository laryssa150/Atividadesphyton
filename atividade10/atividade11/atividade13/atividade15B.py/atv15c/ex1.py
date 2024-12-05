'''
Crie um programa que solicite ao usuário um número inteiro n e imprima um quadrado de asteriscos (*) de tamanho n x n.
'''

n = int(input("digite um número:"))
numero= 1

while numero <=n:
 print("*"*n)
 numero+=1
numero = n
while numero <n:
 print("*"*n)
 numero-=1