"""
Un conjunto es una coleccion desordenada de elementos unicos
Los conjuntos se definien utilizando {}
son mutables
"""
numeros={20,1,2,40,3,4,5,20}
set1={1,2,3}
set2={3,4,5}
union = set1 | set2 #union
#print(union)
interseccion= set1 & set2
#print(interseccion)

set1.add(4)#Agrega un solo elemento al conjunto
mi_set={1,2,3}
mi_set.update([4,5,6])#Actualizar el conjunto
mi_set.remove(2)#Remover un elemento del conjunto
mi_set.clear()
print(mi_set)

#=============""
#Metodo Union
set1={1,2,3}
set2={4,5,6}
union_set=set1.union(set2)
#Metodo Intersection
set1={1,2,3}
set2={3,5,6}
intersection_set=set1.intersection(set2)
#Metodo Diferencia
set1={1,2,3}
set2={3,5,6}
diferencia_set=set1.difference(set)








