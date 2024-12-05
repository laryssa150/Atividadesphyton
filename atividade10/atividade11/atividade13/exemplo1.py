nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
print("Escolha a categoria dos sintomas:")
print("1: Sintomas graves (ex: fraturas, sangramentos)")
print("2: Sintomas emergenciais (ex: dor intensa, dificuldade respiratória)")
print("3: Sem classificação")
sintomas = input("Digite ")


if sintomas == "1":
    if idade <= 12 or idade > 65:
        print("Classificação: Emergência Preferencial")
    else:
        print("Classificação: Emergência")
elif sintomas == "2":
    if idade <= 12 or idade > 65:
        print("Classificação: Grave Preferencial")
    else:
        print("Classificação: Grave")
elif sintomas == "3":
    print("Classificação: Sem classificação")
else:
    print("Opção inválida.")