# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 15:37:05 2021

@author: Andres Marulanda
"""

def actualizar_estado_editor(operaciones):

    texto_escrito = []
    rehacer = []
    texto_actual = " "
    cadena_final = " "

    if len(operaciones) == 0:
        print("Lista vacia")
    
    for i in operaciones:
    
        if i == 'REHACER':
            texto_escrito.append(texto_actual)
            texto_actual = rehacer.pop()
        
        elif i == 'DESHACER':
            rehacer.append(texto_actual)                         
            texto_actual = texto_escrito.pop()               
        
        else:                         
            texto_escrito.append(texto_actual)
            texto_actual = i

    if len(rehacer) != 0:
        rehacer.clear()

    for i in texto_escrito:
        cadena_final += i 
    
    cadena_final = cadena_final + texto_actual  
    return cadena_final


operaciones_usuario = ["Definamos qué es una función de Python: ","Una función es ",
                "un arreglo unidimensional de datos", "DESHACER", "DESHACER", "REHACER", 
                "un grupo de instrucciones"]

cadena = actualizar_estado_editor(operaciones_usuario)
print(cadena)     