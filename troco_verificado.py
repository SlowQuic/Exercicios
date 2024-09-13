print("Preço unitário do produto:")
preco = float(input())
print("Quantidade comprada:")
quantidade = int(input())
print("Dinheiro recebido:")
pagamento = float(input())

precofinal = preco * quantidade
troco = precofinal - pagamento

if precofinal <= pagamento:
    troco = pagamento - precofinal
    print(f"TROCO: {troco:.2f}")
else:
    print(f"DINHEIRO INSUFICIENTE. FALTAM {troco:.2f}")


#Preço unitário do produto: 8.00
#Quantidade comprada: 2
#Dinheiro recebido: 20.00
#TROCO = 4.00

#Preço unitário do produto: 30.00
#Quantidade comprada: 3
#Dinheiro recebido: 70.00
#DINHEIRO INSUFICIENTE. FALTAM 20.00 REAIS 