print("Primeiro valor:")
a = int(input())
print("Segundo valor:")
b = int(input())
print("Terceiro valor")
c = int(input())

if a < b and a < c:
   menor = a
elif b < a and b < c:
   menor = b
else:
   menor = c

print(f"MENOR: {menor:.2f}")      




#Primeiro valor: 7
#Segundo valor: 3
#Terceiro valor: 8
#MENOR = 3 