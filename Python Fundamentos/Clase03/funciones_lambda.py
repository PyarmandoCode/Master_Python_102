"""
Son Funciones Anonimas funciones sin nombre
se definenes utilizando la palabra clave lambda
se usan para realizar operaciones simples y rapidas.
- map()
- filter()
- reduce()
sintaxis:
lambda argumentos: expresion
"""
suma= lambda a,b:a+b
print(suma(5,3))

cuadrado= lambda x: x**2
print(cuadrado(3))

es_par=lambda x: x % 2==0
print(es_par(7))
