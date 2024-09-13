print("Digite a duracao em segundos:")
duracao = int(input())

horas = duracao // 3600
resto = duracao % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{horas:02}:{minutos:02}:{segundos:02}")