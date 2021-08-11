# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 12:23:57 2021

@author: Andres Marulanda
"""

""" RPOGRAMA PARA PROBAR FUNCIONES"""

import primo_MCD_mcm as pmm

a = int(input("Ingrese el primer entero: "))
b = int(input("Ingrese el segundo entero: "))
    
if pmm.primo(a):
    print("\nEl número es primo")
else:
    print("\nEl número no es primo")
    
if pmm.primo(b):
    print("\nEl número es primo")
else:
    print("\nEl número no es primo")
    
#Hallar el MCD

mcd = pmm.MCD(a, b)
print("\nEl MCD de ",a ,"y", b, "es: ",mcd)

mcm = pmm.mcm(a, b)
print("\nEl mcm de: ",a ,"y", b, "es: ",mcm)

