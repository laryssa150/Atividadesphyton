'''
Laço for: usamos esse tipo de interação quando sabemos quantas vezes será necessarias o laço acontecer, ou seja, não dependemos de uma condição como o while
'''
#lista_nomes = ["ana","joão","antonia","marcio"]

#for nome in lista_nomes:#para cada nome na lista__nomes
#print(nome)#exibr nome

'''
1-receba nomes de usuários que o usuário digite 0,depois exiba quais desses nomes inicima com a letra A.


lista_nomes = []#cria uma lista vazia
n = input("Digite um  nome:")#solicita o nome ao usuário

while n !='0':#enquanto o nome digitado for diferente de 0
    lista_nomes.append(n)#adiciona o nome digitado  a lista 
    print(lista_nomes)#exibe a nova lista
    n = input("digite um nome:")#pede outro nome

print("lista_final:", lista_nomes)#mostra a lista final

for nome in lista_nomes:
     nome = nome.upper()
if nome.startswith('A'):
    print(nome)
    '''

'''
2- faca um programa que receba 10 números e ao final exiba o dobro do valor digitado, se esse número for maior mque 8.
'''

lista_valores = []

for n in range(10):
    v = int(input("Digite um número:"))
    lista_valores.append(v)
    print(lista_valores)
    if v >8:
        lista_valores.append(v*2)
    else:
        lista_valores.append(v)
        print(lista_valores)

#print(range(10))#a função range cria um intervalo
#print(list(range(10)))

#print("#"*10)

#print(range(2,10))#Determinando o inicio e o fim dpo intervalo
#print(list(range(2,10)))

#determinanod o inicio eo fim do intervalo e o passo

#print(range(1,11,3))
#print(list(range(1,11,3)))