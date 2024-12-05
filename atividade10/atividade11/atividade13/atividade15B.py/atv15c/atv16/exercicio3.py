'''
1)Faça um Programa que leia um vetor de 10 caracteres.  
2)diga quantas consoantes foram lidas. 
3)Imprima as consoantes.
'''

lista = []
somente_vogais = ['a', 'e', 'i', 'o', 'u']
somente_consoantes = []

for v in range(10):
    v = str(input("Digite os caracteres: ")).lower()
    lista.append(v)
    if v not in somente_vogais:
        somente_consoantes.append(v)
    else:
     print(f"As vogais são:{somente_vogais}")

print(f"As consoantes são: {somente_consoantes}")