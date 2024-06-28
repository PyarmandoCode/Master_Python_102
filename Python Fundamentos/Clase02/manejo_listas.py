mi_lista=[50,10,20,30,40]
mi_lista2=["A",20,True,12.67,[12,34,56]]
#SCILING :
#sinataxis secuencia[inicio:fin:paso]
"""
CRUD
C=CREATE
R=LEER
U=UPDATE
D=DELETE
"""
mi_lista.append(78)#un elemento al final de la lista
mi_lista.insert(2,299)#un elemento en la posiscion indicada de la lista
mi_lista[2]=10000 #Actualizando por medio del indice
#print(mi_lista[2]) #Imprimiendo el valor especifico
mi_lista.pop(2)#Elimina un elemento por el indice
mi_lista2.remove("A")#Elimina por su valor
#mi_lista.sort()#ordenar de la ASC
#mi_lista.reverse()#ordenar DSC
#print(mi_lista)
#print(mi_lista[-1])

mi_lista2=[10,20,30,40,50]
sub_lista=mi_lista2[1:4]#1=Inclusive,#4=Exclusive
#print(sub_lista)
cadena="La Flor que sembre en mi jardin tomo en verano un color celeste"
ultimo_35_elementos=cadena[35:]
mi_lista[:3]
print(ultimo_35_elementos)

