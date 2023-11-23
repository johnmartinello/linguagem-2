def is_data_valid(dia, mes, ano):
    if dia < 1 or dia > 30 or mes < 1 or mes > 12 or ano < 1:
        raise ValueError("Data inválida")


try:
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))

    is_data_valid(dia, mes, ano)

    print("Data válida: {}/{}/{}".format(dia, mes, ano))

except ValueError as e:
    print("Erro:", str(e))
