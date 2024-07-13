def leer_achivo():
    with open('E:\Master_Python_102\Python Fundamentos\informacion.txt','r',encoding='utf-8') as file:
        contenido=file.read()
        print(contenido)


def leer_achivo_linea_linea():
    try:
        with open('informacion.txt','r',encoding='utf-8') as file:
            for linea in file:
                print(linea.strip())
    except FileNotFoundError:
        print("El Archivo no existe")            
    except IOError:
        print("Ocurrio un error al leer el archivo")    
    #finally:
        #file.close()    
            

leer_achivo_linea_linea()        