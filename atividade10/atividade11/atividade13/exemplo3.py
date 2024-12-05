x = float(input("Insira a coordenada x: "))
y = float(input("Insira a coordenada y: "))

# Determina o quadrante
if x > 0 and y > 0:
    quadrante = "Quadrante I"
elif x < 0 and y > 0:
    quadrante = "Quadrante II"
elif x < 0 and y < 0:
    quadrante = "Quadrante III"
elif x > 0 and y < 0:
    quadrante = "Quadrante IV"
else:
    quadrante = "O ponto está sobre um dos eixos."

# Calcula a distância até a origem
distancia = (x**2 + y**2) ** 0.5

# Exibe o resultado
print(f"O ponto ({x}, {y}) está no {quadrante}.")
print(f"A distância do ponto até a origem é {distancia:.2f}.")