import tkinter as tk

def sumar():
    num1=float(entrada1.get())
    num2=float(entrada2.get())
    resultado.set(num1+num2)


ventana=tk.Tk()
ventana.title("Calculadora Simple")
ventana.geometry("300x200")

#Variables para las entradas y el resultado
entrada1=tk.Entry(ventana)
entrada1.pack(pady=5)
entrada2=tk.Entry(ventana)
entrada2.pack(pady=5)
resultado=tk.StringVar()

boton=tk.Button(ventana,text="Sumar",command=sumar)
boton.pack(pady=10)

etiqueta_resultado=tk.Label(ventana,textvariable=resultado)
etiqueta_resultado.pack(pady=10)

ventana.mainloop()