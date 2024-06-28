"""
Utilice bucle for cunado conozca las veces que se repetira el proceso

for x in range(2,11,2):
    print(f"{x} Master en Python")
"""
"""
Si encuentra un Numero Impar debe terminar el bucle
numeros=[2,4,12,6,8,9,10]
for numero in numeros:
    if numero % 2 != 0:
        break#Interrumpir la ejecucion del bucle
    print(numero)
"""
#Si encuentro numeros impares voy a saltarlos
numeros=[2,4,12,6,8,9,10]
for numero in numeros:
    if numero % 2 != 0:
        continue#Salto lo ignora
    print(numero)    