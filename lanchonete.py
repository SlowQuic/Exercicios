lista = [0.0, 5.00, 3.50, 4.80, 8.90, 7.32]

print("Código do produto comprado:")
X = int(input())
print("Quantidade comprada:")
quantidade = int(input())

valor = lista[X] * quantidade

print(f"Valor a pagar: R${valor:.2f}")


#1 R$ 5.00 
#2 R$ 3.50 
#3 R$ 4.80 
#4 R$ 8.90 
#5 R$ 7.32 

#Codigo do produto comprado: 1
#Quantidade comprada: 3
#Valor a pagar: R$ 15.00
