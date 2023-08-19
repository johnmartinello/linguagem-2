idade = int(input("idade do nadador: "))

if idade < 5:
    print("menos que 5 anos")

elif idade >= 5 and idade <= 7:
    print("categoria infantil A = 5 - 7 anos")

elif idade >= 8 and idade <= 10:
    print("categoria infantil B = 8-10 anos")

elif idade >= 11 and idade <= 13:
    print("juvenil A = 11-13 anos")

elif idade >= 14 and idade <= 17:
    print("categoria juvenil B = 14-17 anos")

else:
    print("categoria adulto = maiores de 18 anos")
