def excepciones_1():
    try:
        valor1=29
        valor2=0
        resultado=valor1/valor2
    except Exception as err:
        print(err)    
    else:
        print(resultado)  
    finally:
        print("Se cerro el archivo correctamente")     


try:
    num1= int(input("Ingrese numero1"))
    resultado=num1*20
except ValueError:
    print("Valor Ingresado invalido")    
    