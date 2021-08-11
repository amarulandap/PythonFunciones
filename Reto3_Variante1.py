# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 15:21:50 2021

@author: Andres Marulanda
"""

def traductor(msj):
    
    traducido = ""
    codigo_morse = {' ':'/', 'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 
                    'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'---.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 
                    'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '"':'"'}
    
    print(len(codigo_morse))
    
    for i in msj:
            traducido += codigo_morse[i] + " " 
    
    return traducido.rstrip()
    
#variable para almacenar el mensaje a traducir.
msj = ""

#Usuario debe ingresar el programa a traducir para entregarlo a la función.
msj = input("Ingrese el mensaje: ")
MSJ = msj.upper()
print("")
print(MSJ)

print("")
print(traductor(MSJ))









