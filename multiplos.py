print("Digite o valor de dois numeros inteiros:")
X = int(input())
Y = int(input())

if X > Y:
    resultado = X % Y
    if resultado == 0:
        print("São multiplos")
    else:
        print("Não são multiplos")    
else:
    resultado = Y % X   
    if resultado == 0:
        print("São multiplos") 
    else:
        print("Não são multiplos")    