import tkinter as Tk

ventana = Tk.Tk()
ventana.title("Formulario de registro")
ventana.geometry("400x300")

def registro():
    try:
        nombre = entrada1.get()
        edad = int(entrada2.get())
        email = entrada3.get()
        resultado.set(f"Nombre:{nombre}, Edad: {edad}, Email:{email}")
    except ValueError:
        resultado.set("Error: La edad debe ser un número")

resultado = Tk.StringVar() #es una variable especial de tkinter que se usa para crear un enlace entre los widgets y variables Python.
# Labels/etiquetas con mejor espaciado para cada casilla
Tk.Label(ventana, text="Nombre:").pack(pady=(10, 0))
entrada1 = Tk.Entry(ventana)
entrada1.pack(pady=(0, 10))

Tk.Label(ventana, text="Edad:").pack(pady=(0, 0))
entrada2 = Tk.Entry(ventana)
entrada2.pack(pady=(0, 10))

Tk.Label(ventana, text="Email:").pack(pady=(0, 0))
entrada3 = Tk.Entry(ventana)
entrada3.pack(pady=(0, 10))
#Se crea el boton para guarde los registro y se usa command para tomar la funcion creada
Tk.Button(ventana, text="Registrar", command=registro).pack(pady=10)#Directamente llamamos al .pack para su margen

Tk.Label(ventana, textvariable=resultado).pack(pady=10)#Con esta se puede visualizar en la misma ventana el registro

ventana.mainloop()