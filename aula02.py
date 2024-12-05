#variáveis e tipo

'''
Para criar variáveis no python, basta digitar o nome do identificador e usar o simbolo (=) para faxer a articulação, apos isso
é só colocar o valor que deseja armazenar>

em python,as variáveis são dinamicamente tipadas, ou  seja, não precisamos dizer o tipo delas quando a criamos,o q determina essa rtipagem é o que irá ser atribuido>Sendo assim,uma variavel pode guardar um texto(srt)
e depois guardar um numero inteiro(int) por exemplo.
'''

#variaveis do tipo caractere --> sting(str)
produto = "banana"#a sting pode ser atribuida usandpo apenas aspas simples('') ou aspas dupals("")

#variaveis do tipo valor --> float
valor = 4.3#p/ numeros do tipo flutuante (float), usamos o ponto(.)para separar as casas decimais

#variaveis do tipo inteiro --> integer(int)
quantidade = 12 #p/ o tipo inteiro(int),basta escrever o valor sem aspas

#variaveis do tipo logica -->boolean(bool)
#True -->verdadeiro
#False-->falso
temEstoque = True #variaveis do tipo logico(bool) sempre guardam os valores Truerue ou False
#para saber o tipo de uma variavel usamos a funçao type(),dentro dos parenteses passamos #a variavel que queremos saber o tipo 
#print("tipo da variavel produto:", type(produto))
#print("tipo da variavel valor:", type(valor))
#print("tipo da variavel quantidade:", type(quantidade))
#print("tipo da variavel temEstoque:", type(temEstoque))

#operadores aritmeticos
'''
Soma | +
------------
Subtração  | -
----------------
Multiplicação  | *
-------------------
Divisão | /
---------------
Divisão Truncada (inteira)| //
-------------------
potencia | **
-----------------
Modulo | % 
'''
#por default (padrão), todo input é uma string
n1 = int(input("Digite um número: "))#int()transforma o valor para inteiro

#float()transforma o valor para real
n2 = input("Digite outro número:")
n2 = float(n2)

#o mais (+) pode ser usado para somar (quando usado para numeros)
# e para concatenar (quando usamos em strings)
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1/ n2
divTrun = n1 // n2
mod = n1 % n2
pot = n1 ** n2
#print("soma", n1, "+", n2, "=", soma)#forma concatenada
#print(f"Subtração:{n1} - {n2} = {sub}")#forma interpoada

#Operadores Relacionais
'''
Igual | ==
---------
diferente | !=
--------------
Maior que | >
------------
Menor que | <
Menor igual | <=
'''

#Operadores lógicos
'''
E | and
-------
OU | or
-------
NÂO | not
--------
'''

