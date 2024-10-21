#A)
def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]
    return soma

#B)
def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][-i]
    return soma

#C)
def soma_diagonal_principal(matriz):
    soma = 0
    for linha in matriz:
        for elemento in linha:
            soma += elemento
    return soma

#D)
def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][len(matriz)-i-1]
    return soma

#E)
def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[len(matriz)-i-1][i]
    return soma