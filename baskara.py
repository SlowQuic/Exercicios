import math
print("Digite o coeficiente a")
a = float(input())
print("Digite o coeficiente b")
b = float(input())
print("Digite o coeficiente c")
c = float(input())

delta = (b ** 2) - (4 * a * c)

if delta >= 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"X1: {x1:.4f}")
    print(f"X2: {x2:.4f}")
else:
    print("Esta equacao nao possui raizes reais")