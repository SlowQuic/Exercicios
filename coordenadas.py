print("Valor de X:")
X = float(input())
print("Valor de Y:")
Y = float(input())


if X == 0 and Y == 0:
    print("Origem")
elif X > 0 and Y > 0:
    print("Q1")
elif X > 0 and Y < 0:
    print("Q4")
elif X < 0 and Y > 0:
    print("Q2")
elif X < 0 and Y < 0:
    print("Q3")
elif X != 0 and Y == 0:
    print("Eixo X")
else:
    print("Eixo Y") 
                                   

#Q1 = X+ e Y+
#Q2 = X- e Y+
#Q3 = X- e Y-
#Q4 = X+ e Y-
#Origem = 0 e 0
#EixoX = X+- e 0
#EixoY = 0 e Y+-
