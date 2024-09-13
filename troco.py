print("Preço unitário do produto:")
preco = float(input())
print("Quantidade comprada:")
quantidade = int(input())
print("Dinheiro recebido:")
pagamento = float(input())

troco =  pagamento - (preco * quantidade)

print("TROCO:", troco)



#Preço unitário do produto: 8.00
#Quantidade comprada: 2
#Dinheiro recebido: 20.00
#TROCO = 4.00