'''
time-profiler lib
import time
start = time.()
end = time.()
duration = end - start
'''

#Solução 1
def sol1_tem_duplicados(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

#Solução 2
def sol2_tem_duplicados(lista):
    lista_ordenada = sorted(lista)
    for i in range(len(lista_ordenada) - 1):
        if lista_ordenada[i] == lista_ordenada[i + 1]:
            return True
    return False

#Solução 3
def sol3_tem_duplicados(lista):
    elementos_vistos = set()
    for elemento in lista:
        if elemento in elementos_vistos:
            return True
        elementos_vistos.add(elemento)
    return False



