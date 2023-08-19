n = int(input("digite os segundos: "))

horas = int((n/60)/60)
minutos = int((n/60)-60*horas)
segundos = int(n - (minutos*60) - ((horas*60)*60))

print(f"{horas} horas, {minutos} minutos e {segundos} segundos")
