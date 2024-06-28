"""
INMUTABLE
Tuplas
"""
valores=(20,50,80)

mi_lista=list()#Objeto List

mi_lista=list(valores)#Tupla convertirlo a lista
mi_lista.append(120)#Añadir el valor
valores=tuple(mi_lista)#Converti a tupla
print(valores)
