print("Digite as três distâncias:")
x1 = float(input()) 
x2 = float(input()) 
x3 = float(input()) 

if x1 > x2 and x1 > x3:
    maior = x1
elif x2 > x1 and x2 > x3:
    maior = x2
else:
    maior = x3       

print(f"MAIOR DISTANCIA: {maior:.2f}") 

#Digite as tres distancias: 
#83.21 
#79.53 
#89.15 
#MAIOR DISTANCIA = 89.15