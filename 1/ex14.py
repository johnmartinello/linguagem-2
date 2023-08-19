min = int(input("digite quantos minutos durou a chamada: "))

if min <= 3:
    print("chamada custou R$1,15")

else:
    dif = min - 3
    valor = (dif * 0.26) + 1.15
    print(f"chamada custou R${round(valor,2)}")
