import tkinter as tk
from tkinter import ttk

def iniciar_progreso():
    for i in range(101):
        barra_progreso["value"]=i #Incrementando el progreso
        root.update_idletasks()#Actualizar la Ventana 
        root.after(50)#Espera de 50 ms

root=tk.Tk()
root.title("Barra de Progreso")
root.geometry("300x200")

#Crear una barra de progreso
barra_progreso=ttk.Progressbar(root,orient="horizontal",length=200,mode="determinate")
barra_progreso.pack(pady=10)

#Crear un boton para iniciar la barra de progreso
boton=tk.Button(root,text="Ingresar al sistema",command=iniciar_progreso)
boton.pack(pady=10)

root.mainloop()