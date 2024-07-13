"""
Funciones Matematicas
"""
import math
#print(math.pi)
#print(math.sqrt(20))
#print(math.cos(math.pi/3))

"""
Funciones Estadisticas
"""
import statistics
datos=[2.90,10.5,14.7,23.7,10.5]
media=statistics.mean(datos)
valor_medio=statistics.median(datos)
variance=statistics.variance(datos)
valor_moda=statistics.mode(datos)
#print(round(media,2))


"""
Funciones Aleatorias
"""
import random
numero=random.randrange(1,100)
cursos=["PYTHON","DJANGO","FLASK","MA"]
curso=random.choice(cursos)
#print(curso)


import sys

print("Version de Python",sys.version)
print("Informacion de la Version",sys.version_info)
print("Plataforma",sys.platform)

entrada=sys.stdin.read()
print("Lo que se escribio fue",entrada)

sys.exit()