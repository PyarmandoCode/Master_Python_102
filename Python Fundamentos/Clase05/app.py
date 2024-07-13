import contactos_logica as cl

#interfaz usuario

def mostrar_menu():
    print("\nGestor de Contactos")
    print("1.-Añadir Contactos")
    print("2.-Ver Contactos")
    print("3.-Actualizar Contactos")
    print("4.-Eliminar Contacto")
    print("5.-Salir")

def ejecutar():
    while True:
        mostrar_menu()
        opcion=input("Seleccione una Opcion:")    
        if opcion=="1":
            nombre=input("Nombre:")
            telefono=input("Telefono:")
            email=input("Email:")
            cl.añadir_contacto(nombre,telefono,email)
        elif opcion=="2":
            cl.ver_contactos() 
        elif opcion =="3":
            cl.ver_contactos()
            indice=int(input("Seleccione el indice del contacto actualizar:")) 
            nombre=input("Nuevo Nombre (deja en blanco para no cambiarlo):")   
            telefono=input("Nuevo Telefono (deja en blanco para no cambiarlo):")   
            email=input("Nuevo Email (deja en blanco para no cambiarlo):")   
            cl.actualizar_contacto(indice,nombre if nombre else None,telefono if telefono else None,email if email else None)
        elif opcion=="4":
            cl.ver_contactos()
            indice=int(input("Seleccione el indice del contacto a eliminar:"))    
            cl.eliminar_contacto(indice)
        elif opcion=="5":
            print("Saliendo...")       
            break
        else:
            print("Opcion no valida , intente de nuevo")

ejecutar()            

