import numpy as np

"""Inicio espacio para programar funciones propias"""


"""Fin espacio para programar funciones propias"""

def solucion(A):
    n = A.shape[0]
    valor_minimo = A[0][1]
    for i in range(0, n):
        for j in range(0, n - i):
            if (i + j)%2 != 0:
                #valor_minimo = A.min()
                if A[i][j] <= valor_minimo:
                    valor_minimo = A[i][j]
                    
    posiciones_valor_minimo = []
    for i in range(0, n):
        for j in range(0, n - i):
            if (i + j)%2 != 0 and A[i][j] == valor_minimo:
                posiciones_valor_minimo.append((i,j))
                
    return valor_minimo, posiciones_valor_minimo
    
"""
Estas líneas de código que siguen, permiten probar si su ejercicio es correcto
"""
#NO MODIFICAR
matriz_entrada = np.array([[89, 13, 23, 72],
       [29, 11, 81, 62],
       [27, 26, 88, 33],
       [ 5, 78, 11, 11]])
menor_estudiante = solucion(matriz_entrada)[0]
posiciones_menor_estudiante = solucion(matriz_entrada)[1]
print("MATRIZ ENTREGADA:\n", matriz_entrada,"\n")
print("===SALIDA ESPERADA===\nMenor = ", 5,"\nPosiciones donde está el menor = ", [(3, 0)],"\n")
print("===TU SALIDA===:\nMenor = ", menor_estudiante,"\nPosiciones donde está el menor = ", posiciones_menor_estudiante,"\n")
if menor_estudiante == 5 and  set(posiciones_menor_estudiante) == set([(3, 0)]):
    print("Todo se ve correcto, ¡Procede a calificar tu código!")
else:
    print("Las salidas no coinciden, ¡Estás olvidando algo en tu código!")