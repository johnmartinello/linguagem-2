try:
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    if valor2 <= 0:
        raise ValueError("O segundo valor deve ser maior que zero")

    resultado = valor1 / valor2
    print("Resultado da divisão:", resultado)

except ValueError as e:
    print("Erro:", str(e))

except Exception as e:
    print("Ocorreu uma exceção não tratada:", str(e))
