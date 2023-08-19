x = int(input("numero: "))

if x < 0:
    print(f"{x} eh negativo")

elif x > 0:
    print(f"{x} eh positivo")
else:
    print("zero")

if x % 2 == 0:
    print(f"{x} eh par")
else:
    print(f"{x} eh impar")
