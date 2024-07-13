def escribir_archivo():
    with open('generado_python.txt','w',encoding='utf-8') as file:
        file.write("Esta es la primera linea.\n")
        file.write("Esta es la segunda linea.\n")
    
escribir_archivo()    