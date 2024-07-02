import csv

with open('E:\Master_Python_102\Python Fundamentos\datos.csv') as archivo_csv:
    lector_csv=csv.reader(archivo_csv)
    for fila in lector_csv:
        print(fila)


