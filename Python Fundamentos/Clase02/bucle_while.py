"""
Se ejecutara mientras la condicion sea verdadera
contador=0
while contador<6:
    print(contador)
    contador +=1
"""    
"""
Crear un script que me permita ejecutar un bucle indefinidamente hasta que
el usuario ingrese "n"
"""
notas=list()#Constructor
while True:
    respuesta=input("Deseas Continuar(S/N):")
    if respuesta=='s':
        nota=int(input("Ingrese la Nota:"))
        notas.append(nota)#Añade elementos a la lista
    else:
        print("Imprimiendo la lista de notas")
        print(notas)
        break

"""
- for: Se utiliza para iterar sobre una secuencia o un rango de números. Es más legible y adecuado cuando se conoce el número de iteraciones.
- while: Se utiliza para repetir un bloque de código mientras una condición booleana sea verdadera. Es más flexible y adecuado cuando la condición de finalización depende de cambios dentro del bucle.
"""    

