# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 10:36:07 2021

@author: Andres Marulanda
"""

"""EJERCICIOS CON FUNCIONES"""

import random

def imprime_vector(vector, mensaje="Vector sin nombre"):
        print("\n", mensaje, end=" ")
        for i in range (0, 100):
            print (vector[i], end=" ")

#Función que retorna los divisores enteros de n entre 1 y n.
def conteo(n):
    divisores = 0
    
    contador = 1
    while contador <= n:
        
        if n % contador == 0:
            divisores += 1
        contador += 1
    
    return divisores

#Función para encontrar números perfectos
def perfecto(n):
    suma_divisores = 0
    
    contador = 1
    while contador < n:
        
        if n % contador == 0:
            suma_divisores += contador
        contador += 1
        
    if suma_divisores == n:
        return True
    else:
        return False
    
#Función para comparar el cuadrado de un número con la suma de los primeros n impares.
def cuad(n):
    suma = 0
    m = n ** 2
    
    for i in range(1, 2*n):
        if i % 2 != 0:
            suma += i
        
    if m == suma:
        print("\nEl cuadrado de ",n," es ",m, "=", suma)
    else:
        print("\nEl cuadrado de ",n," es ",m, " != ", suma)
        
#Función para crear una secuencia de numeros donde p4 = p1 + p2 + p3.
def secuencia1(n):
    v = [0] * (n+1)
    
    for i in range(0, n):
        v[i] = 1
        if i >= 3:
            v[i] = v[i-1] + v[i-2] + v[i-3]
            
    print(v)
    
#Función para jugar lance el dado hasta que caiga su número.
def alfin(n):
    lanzamientos = 0
    dado = 0
    
    x = 0
    while x != n:
        dado = random.randint(1,6)
        if n != dado:
            lanzamientos += 1
        else:
            x = n
            
    return lanzamientos
    
     

