#Operadores Ternario Simple
x=2
result=f"{x} es mayor que 5" if x>5 else f"{x} no es mayor que 5"
print(result)

#Operador ternario Anidado
x=5
result="x es mayor que 5" if x>5 else ("x es igual a 5" if x==5 else "x es menor que 5")