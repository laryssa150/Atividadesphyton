#Listas

idades = [15,25,26,30,40]#criando uma lista => []
#essa lista tem 5 itens e 4 posições (0 á 4)

print('Lista', idades)#exibindo a lista

#print('posição 0:')
#print(idades[0])#exibibe a posição 0 da lista
#print('Posição 2:')
#print(idades[2])#exibe a posição 2 da lista
#print('Posição 4:')
#print(idades[4])#exibe a posição 4 da lista

#idades [2] = 25#Alterando o valor de um item na lista
#print(idades)

#len()determinar o tamamho da lista,onde o n é o nome da lista
print(len(idades))

idades.append(50)#inserindo novo item no final da lista
print("append(50):", idades)

idades.insert(0, 1)#inserindo novo item em uma posição desejada, onde o primeiro valor 
#é a posição e o segundo valor é o item a ser inserido
print("insert(0, 1):", idades)

idades.remove(30)#remove um item por posicão da lista
print("remove(30):", idades)

del idades[1]#remove um item por posição da lista
print("del idades[1]:", idades)

#Somar todos os valores de lista => sum()
soma = sum(idades)
print("Soma todos os valores dentro da lista:", soma)

#slicing fatia a lista em uma menor com base no intervalo
novaLista = idades[2:4]
print("idades[2:4]", novaLista)

#Posição inversa
print("idades[-1]: ",idades[-1])
print("idades[-4]: ",idades[-4])
print("idades[-5]: ",idades[-5])

#inveryendo  a lista
idades_inversas = idades [::-1]
print("idades_inversas:",idades_inversas)

#Ordenando a lista
idades_ordenadas = sorted(idades_inversas)
print("idades ordenadas =>sorted(idades_inversas):", idades_ordenadas)

novaLista = [30,20,80,1,50]
print('Lista', novaLista)

crescente = sorted(novaLista)
print('crescente:', crescente)   

#reverse=True faz com que a lista sej ordenada de forma decrescente
decrescente = sorted(novaLista,reverse=True)
print('decrescente:', decrescente)