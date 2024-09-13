print("Você vai digitar a temperatura em qual escala (C/F)?")

while true:
tipo = input()
if tipo == "F":
    print("Digite a temperatura em Fahrenheit:")
    x = float(input())
    resultado = (x * 9/5) + 32
    print(f"Temperatura equivalente em Celsius: {resultado:.2f}")
elif tipo == "C":
    print("Digite a temperatura em Celsius:")
    x = float(input())
    resultado = (x - 32) * 5/9
    print(f"Temperatura equivalente em Fahrenheit: {resultado:.2f}")
else:
    print("INVALIDO")        



#F = (°C * 9/5) + 32
#C = (°F - 32) * 5/9
#Voce vai digitar a temperatura em qual escala (C/F)? F
#Digite a temperatura em Fahrenheit: 75.00
#Temperatura equivalente em Celsius: 23.89 