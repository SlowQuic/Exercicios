print("Digite o salário da pessoa:")
salario = float(input())

if salario <= 1000.00:
    porcentagem = 0.20
    porcentos = "20%"
elif salario <= 3000.00:
    porcentagem = 0.15
    porcentos = "15%"
elif salario <= 8000.00:
    porcentagem = 0.10
    porcentos = "10%"
else:
    porcentagem = 0.05
    porcentos = "5%"

aumento = salario * porcentagem
novosalario = salario + aumento

print(f"Novo salário: R$ {novosalario:.2f}")
print(f"Aumento: R$ {aumento:.2f}")
print("Porcentagem:", porcentos)