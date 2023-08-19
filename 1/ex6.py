cod = int(input("digite o codigo: "))
qnt = int(input("digite a quantidade: "))

if cod == 100:
    valor = qnt * 1.2

elif cod == 101:
    valor = qnt * 1.3

elif cod == 102:
    valor = qnt * 1.5

elif cod == 103:
    valor = qnt * 1.2

elif cod == 104:
    valor = qnt * 1.3

elif cod == 105:
    valor = qnt * 1

print(f"{qnt} unidade(s) do codigo {cod}. Valor total: R${valor}")
