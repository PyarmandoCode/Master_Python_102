"""
Es una Libreria de nucleo de Python
que me permite crear interfaces(Ventanas)
y encima de esas ventanas se pueden dibujar controles(widgets)
Documentacion
https://docs.python.org/3/library/tkinter.html
"""
import tkinter as tk

#Funcion que contiene la logica que tendra el boton
def mostrar_texto():
    texto=entrada.get()
    print("Texto Ingresado",texto)

#Creando una Instancia
root=tk.Tk()

#Establecer el titulo de la ventana
root.title("Ventana Simple")
#Establecer las dimenciones de la ventana
root.geometry("300x200")

#Crear una etiqueta
etiqueta=tk.Label(root,text="Presione el boton")
etiqueta.pack(pady=10)

#Crear una entrada de Texto
entrada=tk.Entry(root)
entrada.pack(pady=10)


#Crear un Boton
boton=tk.Button(root,text="Saludar",command=mostrar_texto)
boton.pack(pady=10)

#Iniciar el Bucle principal de eventos
root.mainloop()


