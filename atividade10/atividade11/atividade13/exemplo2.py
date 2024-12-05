print("Bem-vindo ao Jogo de Perguntas!")
    
pontuacao = 0

    # Perguntas e respostas
    # Pergunta 1
print("\nPergunta 1: Quantos planetas Terra cabem dentro do Sol?")
print("A) Um milhão")
print("B) Cem")
print("C) Seiscentos")
print("D) Cento e cinquenta")
resposta = input("Escolha uma opção (A, B, C, D): ").strip().upper()
    
if resposta == "A":
    pontuacao += 2
    print("Resposta correta! Pontuação atual:", pontuacao)
else:
    print("Resposta incorreta! Pontuação atual:", pontuacao)

    # Pergunta 2
print("\nPergunta 2: Quantos braços tem um polvo??")
print("A) 6")
print("B) 4")
print("C) 5")
print("D) 8")
resposta = input("Escolha uma opção (A, B, C, D): ").strip().upper()
    
if resposta == "D":
    pontuacao += 2
    print("Resposta correta! Pontuação atual:", pontuacao)
else:
    print("Resposta incorreta! Pontuação atual:", pontuacao)
    # Pergunta 3
print("\nPergunta 3: Qual é a capital da França?")
print("A) Londres")
print("B) Berlim")
print("C) Paris")
print("D) Madrid")
resposta = input("Escolha uma opção (A, B, C, D): ").strip().upper()
    
if resposta == "C":
    pontuacao += 2
    print("Resposta correta! Pontuação atual:", pontuacao)
else:
    print("Resposta incorreta! Pontuação atual:", pontuacao)
    # Pergunta 4
print("\nPergunta 4:  Qual o maior planeta do sistema solar?")
print("A) Marte")
print("B) Vênus")
print("C) Saturno")
print("D) Jupiter")
resposta = input("Escolha uma opção (A, B, C, D): ").strip().upper()
    
if resposta == "D":
    pontuacao += 2
    print("Resposta correta! Pontuação atual:", pontuacao)
else:
    print("Resposta incorreta! Pontuação atual:", pontuacao)
    # Pergunta 5
print("\nPergunta 5: Quantos ossos temos no nosso corpo?")
print("A) 180")
print("B) 106")
print("C) 206")
print("D) 215")
resposta = input("Escolha uma opção (A, B, C, D): ").strip().upper()
    
if resposta == "C":
    pontuacao += 2
    print("Resposta correta! Pontuação atual:", pontuacao)
else:
    print("Resposta incorreta! Pontuação atual:", pontuacao)


    # Pergunta Bônus
print("\nPergunta Bônus: Quanto mede uma girafa?")
print("A) Entre 4,8 e 5,5 metros")
print("B) 2 metros")
print("C) Entre 5 e 6 metros")
print("D) 4 metros")
resposta_bon = input("Escolha uma opção (A, B, C, D): ").strip().upper()

if resposta_bon == "A":
    pontuacao += 3
    print("Resposta correta na pergunta bônus! Pontuação atual:", pontuacao)
else:
    pontuacao -= 1
    print("Resposta incorreta na pergunta bônus! Pontuação atual:", pontuacao)

    # Exibir pontuação final e recompensa
print("\n--- Resultados Finais ---")
print(f"Pontuação total: {pontuacao}")

if pontuacao >= 10:
    print("Você é um mestre!")
elif pontuacao >= 9:
    print("Recompensa de Ouro")
elif pontuacao >= 6:
    print("Recompensa de Prata")
elif pontuacao >= 3:
    print("Recompensa de Bronze")
else:
    print("Sem recompensa")