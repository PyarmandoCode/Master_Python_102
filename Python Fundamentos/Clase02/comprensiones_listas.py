"""
Es Una Manera mas compacta y eficinete de usar bucles tradicionales
Sintaxis
[expresion for elemento in iterable]
"""
#Crear una Lista de Numeros de 0 a 9
# for x in range(0,10):
#     print(x)

numeros=[x for x in range(10)]
#print(numeros)

numeros=[x**2 for x in range(10)]
#print(numeros)

pares=[x for x in range(10) if x % 2 ==0]
#print(pares)

palabras=["PYTHON","DJANGO","FLASK"]
minusculas=[palabra.lower() for palabra in palabras]

palabras=[" PYTHON "," DJANGO "," FLASK "]
sin_espacios=[palabra.strip() for palabra in palabras]
print(sin_espacios)



