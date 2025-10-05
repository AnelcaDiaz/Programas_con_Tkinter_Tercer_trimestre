print("Ejercicio 4: Contador de Clics")
import tkinter as Tk 

ventana = Tk.Tk()
ventana.title("Contador de Clics")
ventana.geometry("400x300")

contador = 0
def contar():
    global contador  # Indica que se usará la variable contador como global
    contador += 1
    etiqueta.config(text=str(contador))

def reiniciar(): #Definimos una nueva funcion para reiniciar el contador
    global contador
    contador = 0
    etiqueta.config(text=str(contador))

# Etiqueta que muestra el contador
etiqueta = Tk.Label(ventana, text=str(contador), font=("Calibri", 50))
etiqueta.pack(pady=20)

# Botón para contar
boton = Tk.Button(ventana, text="Clic", font=("Calibri", 20), command=contar)
boton.pack(pady=10)

# Botón para reiniciar
boton_reiniciar = Tk.Button(ventana, text="Reiniciar", font=("Calibri", 12), command=reiniciar)
boton_reiniciar.pack(pady=10)

ventana.mainloop()