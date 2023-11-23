try:
    valor = input("Digite um valor: ")

    if not valor.isdigit():
        raise ValueError("O programa aceita apenas valores inteiros")

    valor = int(valor)

    if valor <= 0:
        raise Exception("ValorAbaixoException: Valor menor ou igual a 0")

    elif 100 < valor < 1000:
        raise Exception("ValorAltoException")

    elif valor >= 1000:
        raise Exception("ValorMuitoAltoException")

    print("Valor inserido:", valor)

except ValueError as e:
    print("Erro:", str(e))

except Exception as e:
    print("Erro:", str(e))
