import math
print("Base do retangulo:")
base_str = input()
base = float(base_str)
print("Altura do retangulo:")
altura_str = input()
altura = float(altura_str)

area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt(base**2 + altura**2)

print(f"AREA: {area:.4f}")
print(f"PERIMETRO: {perimetro:.4f}")
print(f"Diagonal: {diagonal:.4f}")