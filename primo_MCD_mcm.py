# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 12:06:41 2021

@author: Andres Marulanda
"""

"""OPERACIONES CON ENTEROS"""

"""1. Determinar si un número es primo"""

import math


def primo(x):
    if x % 2 == 0:
        return False
    
    i = 3
    while i <= math.sqrt(x):
        if x % i == 0:
            return False
        i +=2
        
    return True

"""2. Máximo comun divisor"""

def MCD(x, y):
    res = x % y
    
    while res != 0:
        x = y
        y = res
        res = x % y
        
    return y

"""3. Mínimo común multiplo"""

def mcm(x, y):
    r = x * y // MCD(x, y)
    return r

"""4. Determinar el primer digito de un entero"""

def pd(x):
    
    r = 0
    while x < 9:
        r = x // 10
    return r


