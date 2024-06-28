mi_diccionario={}
mi_diccionario=dict()

mi_diccionario = {
    "nombre":"Juan",
    "edad":30,
    "ciudad":"california"
}

#print(mi_diccionario.get("nombre"))
#print(mi_diccionario.get("edad"))
#print(mi_diccionario.get("ciudad"))

print(mi_diccionario.keys())
print(mi_diccionario.values())

for k,v in mi_diccionario.items():
    print(f"La clave {k} y su valor {v}")

"""
En Python, los tipos de datos se dividen en dos categorías: mutables e inmutables. La diferencia principal entre ellos radica en si el objeto puede ser modificado después de su creación.

Tipos de Datos Mutables
=========================
Los objetos mutables pueden ser modificados después de su creación. Esto significa que su contenido o estado interno puede cambiar sin necesidad de crear un nuevo objeto. Algunos ejemplos comunes de tipos de datos mutables en Python son:

-Listas (list)
-Diccionarios (dict)
-Conjuntos (set)
-Objetos definidos por el usuario

Tipos de Datos Inmutables
===========================
Los objetos inmutables no pueden ser modificados después de su creación. Cualquier operación que parezca modificar un objeto inmutable en realidad crea un nuevo objeto. Algunos ejemplos comunes de tipos de datos inmutables en Python son:

- Enteros (int)
- Flotantes (float)
- Cadenas de texto (str)
- Tuplas (tuple)
- Conjuntos inmutables (frozenset)
- Bytes (bytes)



"""    