'''
Faça um Programa que peça as quatro notas de 3 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0
'''

lista_notas=[]
lista_alunos=[0,lista_notas]

while lista_alunos[0]<=3:
    lista_alunos[0]+=1

    for n in range(4):
        v= float(input("Digite as notas dos alunos: "))
        lista_notas.append(v)
        print(lista_alunos)
    media = sum(lista_notas )/4
    if media >=7:
    
        print(f"Vc foi aprovado:{media}")
    else:
        print(f"Vc foi reprovado:{media}")

    del lista_notas[0:5]