print("Digite a quantidade de minutos:")
minutos = int(input())

if minutos <= 100:
    print("Valor a pagar: R$ 50.00")
else:
    preco = (minutos - 100) * 2 + 50
    print(f"Valor a pagar: R${preco:.2f}") 
    
        



#Digite a quantidade de minutos: 22
#Valor a pagar: R$ 50.00

#Digite a quantidade de minutos: 103
#Valor a pagar: R$ 56.00 