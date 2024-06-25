#Definicion de Variables
x= 5 # entero
y = 3.2 #flotante
name= "John" #cadena de Texto
is_student=True #booleano

#imprimir variables
"""
print(x)
print(y)
print(name)
print(is_student)
"""

#Estructuras de control
#Condicionales -identacion
"""
age=18
if age < 18:
    print("Menor de Edad")
elif age == 18:
    print("Exactamente 18 Años")
else:
    print("Mayor de edad") 
"""
#Bucles 
"""
#Bucle for
for i in range(1,15,2): #imprimir numeros del 0 al 4
    print(i)
#Bucle while
count=0
while count <5: #True salir del bucle
    print(count)#0 1 2 3 4 5  
    count +=1
"""
#Funciones
"""
def welcome(name,curso):
    return f"Hola ,{name} Bienvenido al curso Master {curso}"
    
print(welcome("Carmen","Django"))
"""
"""
#Estructura de datos
#Listas
#Diccionarios
#Tuplas
#Conjuntos
fruits=["manzana","banana","cereza"]#list
#print(fruits[1:2])
#for fruit in fruits:
#    print(fruit)
#Diccionarios
person = {
    "nombre":"Alice",
    "edad":23,
    "ciudad":"Madrid"
}
print(person.get("nombre"))
"""
"""
Operadores Aritmeticos
Operadores de suma, resta, multiplicación y división:
Suma: +
Ejemplo: a + b

Resta: -
Ejemplo: a - b

Multiplicación: *
Ejemplo: a * b

División decimal: /
Ejemplo: a / b

División entera: //
Ejemplo: a // b (Devuelve el cociente entero de la división)

Módulo: %
Ejemplo: a % b (Devuelve el residuo de la división)

Exponente: **
Ejemplo: a ** b (Calcula a elevado a la potencia b)


base=2
exponente=3
res=base ** exponente
#print(f"{base} elevado al {exponente} es igual al {res}")

resultado_dec= 23 / 5
resultado_ent= 23 // 5
print(f"el resultado de la division con decimales {resultado_dec}")
print(f"el resultado de la division parte entera {resultado_ent}")
"""
"""
Operadores de comparación:
Igualdad: ==
Desigualdad: !=
Mayor que: >
Menor que: <
Mayor o igual que: >=
Menor o igual que: <=

Operadores Logicos:
and: Devuelve True si ambas expresiones son verdaderas.
or: Devuelve True si al menos una de las expresiones es verdadera.
not: Niega la expresión booleana; devuelve False si la expresión es verdadera y viceversa.

"""
"""
#Funcion Input
precio = float(input("Ingrese el precio:"))#cats
cant = int(input("Ingrese la Cantidad:"))
total = precio * cant
print(f"el total del producto a pagar es {total}")
print(type(precio))
print(type(cant))
"""

x= 5 # entero
y = 3.2 #flotante
name= "John" #cadena de Texto
is_student=True #booleano

print(f"{x} {y} el nombre es {name}  es estudiante ?{is_student}")