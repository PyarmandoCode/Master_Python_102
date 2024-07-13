import json
#Lista para almacenar los contactos
contactos=[]

#Cargar los contactos desde un archivo JSON

try:
    with open('E:\Master_Python_102\Python Fundamentos\contactos.json','r') as file:
        contactos=json.load(file)
except FileNotFoundError:
    print("El Archivo no se encontro")        
    contactos=[]

#Ver todos los contactos
def ver_contactos():
    if not contactos:
        print("No Hay Contactos")
    for idx,contacto in enumerate(contactos,start=1):
        print(f"{idx} .Nombre :{contacto['nombre']},Telefono:{contacto['telefono']} Email: {contacto['email']} ")

#Funcion para guardar los contactos en un archivo json
def guardar_contactos():
    with open('E:\Master_Python_102\Python Fundamentos\contactos.json','w') as file:
        json.dump(contactos,file,indent=4)

#Añadir un contacto
def añadir_contacto(nombre,telefono,mail):
     new_contacto= {
        "nombre":nombre,
        "telefono":telefono,
        "email":mail
     }     
     #Añades a lista
     contactos.append(new_contacto)  
     #Añades al archivo
     guardar_contactos() 
     print("Contacto añadido con exito...")

def actualizar_contacto(indice,nombre=None,telefono=None,email=None):
    try:
        contacto=contactos[indice-1]
        if nombre:
            contacto['nombre']=nombre
        if telefono:
            contacto['telefono']=telefono
        if email:
            contacto['email']=email
        guardar_contactos()
        print("Contacto actualizado")            
    except IndexError:
        print("Indice No valido")    

def eliminar_contacto(indice):
    try:
        contactos.pop(indice-1)
        guardar_contactos()
        print("Contacto eliminado")
    except IndexError:
        print("Indice Invalido")    