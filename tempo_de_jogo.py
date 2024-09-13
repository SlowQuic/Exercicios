print("Hora inicial:")
inicial = int(input())
print("Hora final:")
final = int(input())

if inicial >= final:
    x = 24 - inicial
    duracao = x + final
    print("O JOGO DUROU", duracao, "HORAS(S)")
else:
    duracao = final - inicial
    print("O JOGO DUROU", duracao, "HORAS(S)")