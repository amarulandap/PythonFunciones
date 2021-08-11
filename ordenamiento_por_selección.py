# -*- coding: utf-8 -*-


def intercambiar(V, i, j):
    aux = V[i]
    V[i] = V[j]
    V[j] = aux

#algoritmo selección
def seleccion(V):
    i=1
    while i < V[0]:
        k = i
        j = i + 1
        while j <= V[0]:
            if V[j] < V[k]:
                k = j
            j = j + 1
        intercambiar(V, i, k)
        i = i + 1
        
#algoritmo de selección con ciclos for
def seleccion2(V):
    for pos_ini in range (1, V[0]):
        pos_menor = pos_ini
        for pos_comp in range (pos_ini + 1, V[0]+1):
            if V[pos_comp]< V[pos_menor]:
                pos_menor = pos_comp
            pos_comp = pos_comp + 1
        intercambiar(V, pos_ini, pos_menor)


vector = [6, 3, 1, 9, 4, 8, 6]
seleccion2(vector)
