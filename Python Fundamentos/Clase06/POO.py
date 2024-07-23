"""
Es un Paradigma de Programacion que utiliza "Objetos"
diseñar aplicaciones y programas.
Objetos son instancias de "clases" que pueden contener
atributos y metodos.
-Modular
-Reutilizable
-Escalable
"""
#Es una plantilla o un modelo para crear objetos.
class Mostro:
    def __init__(self,nombre,descri,nivel,lugar):
        self.nom=nombre
        self.desc=descri
        self.niv=nivel
        self.lug=lugar
    def __str__(self):
         return f"Este Mostro se llama {self.nom} y tiene un nivel de peligrosidad {self.niv}"
    def mostrar_peligrosidad(self):
        if self.niv==1:
            msj="Muy Peligroso"
        elif self.niv==2:
            msj="Peligroso"    
        elif self.niv==3:
            msj="Se le puede combatir"    
        else:
            msj="Facil de Vencer"    
        return msj    
            
#Es una instancia de una clase
Obj_Dracula=Mostro("Dracula","Vampiro",3,"Transilvania")#Instanciar
Obj_Frank=Mostro("Frankeistein","Mutante","2","Georgia")
Obj_Mole=Mostro("Mole","Cuerpo Basado en Rocas",6,"New York")

print(Obj_Mole.mostrar_peligrosidad())

#print(Obj_Dracula.nom)
#print(Obj_Dracula.lug)
#print(Obj_Dracula.__dict__)
#print(Obj_Dracula)
#print(Obj_Mostro2)