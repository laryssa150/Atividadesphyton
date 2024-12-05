valortotal = float(input("Digite o valor total: "))
prestação = int(input("Digite o tanto de parcelas desejadas:"))
juros = int

if(prestação<12):
    print("não terá como pegar o emprestimo") 
elif(prestação==12 or prestação<=24):
    print("não terá juros")
elif(prestação>=24 and prestação<=36):
    juros = (valortotal*10)/100
    print("valor total:", valortotal+juros)
elif (prestação>=36):
  juros = (valortotal*15)/100
  print("valor total:", valortotal+juros)