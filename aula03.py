#condicionais if-elif-else
'''
No python,quando temos condições para realizar açoes,usamos o if-elif-else

SE | if
---------
SENÂO SE | elif
SENÂO | else

sintaxe:
if*condição*:
   *ação*
--------------
elif*condição*:
    *ação*
----------------
else:
  *ação*


*****OBS: O python é uma linguagem de **IDENTAÇÃO OBRIGATÓRIA***, onde é possivel demarcar 
cada bloco com base no recuo da linha
'''
print("1 - aluno")
print("2 - funcionario")
print("3 - visitante")
tipoAcesso = input("Selecione uma opção:")

if tipoAcesso =="1" or tipoAcesso == "2":
 print("acesso liberado")
elif tipoAcesso == "3":
 print("Faça um cadastro para entar!")
else :
 print("Acesso negado!")
