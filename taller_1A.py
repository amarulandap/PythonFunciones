# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 11:08:56 2021

@author: Andres Marulanda
"""

"""" TALLER MISIÓN TIC - VECTORES Y MATRICES"""

import random

"""Funciones para vectores"""

def generar_vector(m):
    v = [0] * (m + 1)
    v[0] = m
    for i in range(1, m+1):
        if i % 2 == 0:
            v[i] = 2*i
        else:
            v[i] = -3*i
    return v

def generar_vector_1(m, r1, r2=None):
    v = [0] * (m+1)
    v[0] = m
    
    for i in range(1, m+1):
        if r2 == None:
            v[i] = random.randint(0,r1)
        else:
            v[i] = random.randint(r1,r2)
            
    return v

def imprimir(v):        
    for j in range(0, n+1):
        print(v[j], end=" ")
    print()
        
def intercambiar(v, i, j):
    aux = v[i]
    v[i] = v[j]
    v[j] = aux
        
    return v


""" Funciones para matrices"""

def crear_matriz(m, n):
    mat = []*(m)
    for i in range(0, m):
        a = [0]*(n)
        mat.append(a)
           
    return mat

def datos_1_9(mat, m, n):
    for i in range(0, m):
        for j in range(0, n):
            mat[i][j] = i+j
            
def cargar_datos_1_11(mat, m, n):
    for i in range(0, m):
        for j in range(0, n):
            mat[i][j] = random.randint(1, 100)

def intercambiar_filas(mat, m, n, a, b):
    for i in range(0, m):
        for j in range(0, n):
            aux = mat[a][j]
            mat[a][j] = mat[b][j]
            mat[b][j] = aux
        
    mat = imprimir_mat(mat, m, n)

def imprimir_mat(mat, m, n):
    for i in range(0, m):
        for j in range(0, n):
            print(mat[i][j], end="\t")
        print()

def matriz_transpuesta(mat, m, n):
    mat1 = crear_matriz(n, m)
    for i in range(0, m):
        for j in range(0, n):
            mat1[j][i] = mat[i][j]
            
    return mat1
        
"""Elabore un programa que inserte un número igual al doble del índice en las posiciones pares 
de un arreglo unidimensional de 50 posiciones; y un número igual al negativo del triple del índice 
en las posiciones impares de dicho arreglo."""

print("\nPROGRAMA PARA IMPRIMIR UN VECTOR DE N POSICIONES")
n = int(input("Ingrese el número de posiciones del vector: "))    
vec1 = generar_vector(n)
imprimir(vec1)



"""Elabore un programa que llene una matriz con números con números iguales a la 
suma de los subíndices de cada elemento"""

print("\nMATRIZ PARA SUMAR LOS VALORES DE LOS SUBINDICES")
m1 = int(input("\nNúmero de filas: "))
n1 = int(input("Número de columnas "))

mat1 = crear_matriz(m1, n1)
datos_1_9(mat1, m1, n1)
#print("\n")
imprimir_mat(mat1, m1, n1)



"""Elabore un programa que intercambie el primer y el tercer elemento de un vector."""

print("\nPROGRAMA PARA INTERCAMBIAR LOS ELMENTOS DE UN VECTOR")
n = int(input("Ingrese el número de posiciones del vector: "))
v_i = generar_vector_1(n, 5, 30)
imprimir(v_i)

a= int(input(f"\nIngrese la primera posición a intercambiar entre 0 y {n}: "))
b= int(input(f"Ingrese la segunda posición a intercambiar entre 0 y {n}: "))
intercambio = intercambiar(v_i, a, b)
print("\n")
imprimir(intercambio)



"""Elabore un programa que intercambie la fila 1 y la fila 3 de una matriz."""

print("\nPROGRAMA PARA INTERCAMBIAR LAS FILAS DE UNA MATRIZ")
m1 = int(input("\nNúmero de filas: "))
n1 = int(input("Número de columnas "))

mat2 = crear_matriz(m1, n1)
cargar_datos_1_11(mat2, m1, n1)
imprimir_mat(mat2, m1, n1)

f1 = int(input("Primera fila que desea intercambiar: "))
f2 = int(input("Segunda fila que desea intercambiar: "))

intercambiar_filas(mat2, m1, n1, f1, f2)



"""Elabore un programa que halle la transpuesta de una matriz."""

print("\nPROGRAMA PARA HALLAR LA TRANSPUESTA DE UNA MATRIZ")
m1 = int(input("\nNúmero de filas: "))
n1 = int(input("Número de columnas "))
            
mat3 = crear_matriz(m1, n1)
cargar_datos_1_11(mat3, m1, n1)
imprimir_mat(mat3, m1, n1)

trans_mat3 = matriz_transpuesta(mat3, m1, n1)
print("\nMatriz transpuesta: ")
imprimir_mat(trans_mat3, n1, m1)


"""La siguiente información corresponde al montaje de una red. 
Usted debe hacer una aplicación que permita almacenar la cotización de los componentes de la red. 
Los datos a almacenar corresponden a Servidor, Cableado, Costo por Terminal, 
Costo anual de energía y Mantenimiento anual."""


