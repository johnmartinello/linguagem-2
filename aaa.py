# Exemplo de matriz 3x3
matriz_exemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Itera pelas linhas da matriz e imprime seus elementos
for linha in matriz_exemplo:
    for elemento in linha:
        print(elemento, end=' ')
    print()  # Imprime uma quebra de linha após cada linha da matriz