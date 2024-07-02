def calcular_edad(nac):
    edad=2024-nac
    return edad

def acceso_sistema(usu,passw):
    if usu=="admin" and passw=="123":
        msj="Bienvenido al Sistema"
    else:
        msj="Error Usuario no reconocido"    
    return msj    

print(acceso_sistema("admin","1234"))
#print(calcular_edad(1975))
