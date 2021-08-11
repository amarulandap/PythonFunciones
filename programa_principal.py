# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 10:36:09 2021

@author: Andres Marulanda
"""

""" PROGRAMA PRINCIPAL"""

import funciones_1

#Programa para hallar cuántos divisores tiene un número.
print("\nCUÁNTOS DIVISORES TIENE UN NÚMERO")

divisores = 0
may_divisores = 1
numero = 0

a = 1
while a <= 100:
    divisores = funciones_1.conteo(a)
    if may_divisores <= divisores:
        may_divisores = divisores
        numero = a
    a += 1

print("El número: ",numero, "tiene mayor número de divisores entre 1 y 100, y son: ",may_divisores, "\n") 

#Programa para hallar los números perfectos.
print("NÚMEROS PERFECTOS ENTRE 1 y 1000")
for i in range(1, 1000):

    if funciones_1.perfecto(i):
        print(i, "Es número perfecto")
    
#Programa para comparar cuadrado con suma de impares.
print("\nEL CUADRDADO DE N ES IGUAL A LA SUMA DE LOS PRIMEROS N NÚMEROS IMPARES")

a = int(input("Ingrese un número entero: "))
funciones_1.cuad(a)

#Programa apara probar la secuencia1.
print("\nSECUENCIA DE NÚMEROS")

c = int(input("Ingrese un número entero: "))
secuencia = [0] * (c + 1)
secuencia = funciones_1.secuencia1(c)

#programa para jugar lance el dado.
print("\nPROGRAMA PARA JUGAR A LANZAR EL DADO")

d = int(input("Ingrese un número entre 1 y 6: "))
while d < 1 or d > 6:
    print("Número incorrecto: ")
    d = int(input("Ingrese un número entre 1 y 6: "))
   
numero_lanzamientos = funciones_1.alfin(d)
print("Número_lanzamientos: ",numero_lanzamientos)




