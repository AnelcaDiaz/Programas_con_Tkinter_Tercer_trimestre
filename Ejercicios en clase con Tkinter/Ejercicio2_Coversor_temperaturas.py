import tkinter as tk

ventana = tk.Tk()
ventana.title("Conversor de temperaturas")
ventana.geometry("400x300")
ventana.config(bg="gold") #Se el asigna un color al fondo de la ventana

def convertir_c_a_f(): #Definimos la funcion convertir de Celcius a fahrenheit 
    try:
        celsius = float(entry_temperatura.get()) #Seo obtiene el valor ingresado en el entry
        fahrenheit = (celsius * 9/5) + 32 #Se realiza la conversion con la formula estandar
        label_resultado.config(text=f"{celsius}°C = {fahrenheit:.2f}°F") #Se muestra el resultado en el label
    except ValueError:
        label_resultado.config(text="¡Error! Ingresa un número válido") #Si no escribe un numero, se muestra el mensaje de error

def convertir_f_a_c(): #Deinimos la otra funcion que seria la inversa de la conversion anterior
    try:
        fahrenheit = float(entry_temperatura.get())
        celsius = (fahrenheit - 32) * 5/9 #Ahora tenemos la formula inversa
        label_resultado.config(text=f"{fahrenheit}°F = {celsius:.2f}°C")
    except ValueError:
        label_resultado.config(text="¡Error! Ingresa un número válido")

# Widgets de la interfaz
label_titulo = tk.Label(ventana, text="Conversor de Temperaturas", bg="gold", font=("Arial", 14, "bold"))
label_titulo.pack(pady=10)#Se crea el titulo de la ventana junto con sus caracteristicas y el pady es para darle un margen vertical

label_instruccion = tk.Label(ventana, text="Ingresa la temperatura:", bg="gold")
label_instruccion.pack(pady=5)#Se crea una etiqueta para las instrucciones y que la visualice el usuario

entry_temperatura = tk.Entry(ventana, font=("Arial", 12))
entry_temperatura.pack(pady=5)#Se determina el entry para que el usuario ingrese la temperatura

# Frame para los botones
frame_botones = tk.Frame(ventana, bg="gold") #Se crea un frame para agrupar los botones
frame_botones.pack(pady=10)

boton1 = tk.Button(frame_botones, text="°C a °F", command=convertir_c_a_f, 
bg="lightcoral", font=("Arial", 10, "bold"), width=12) #Se crea el boton  de la primera conversion y sus caracterisitcas
boton1.pack(side=tk.LEFT, padx=5)#Se posiciona el boton en el frame a la izquierda y se le da un margen horizontal

boton2 = tk.Button(frame_botones, text="°F a °C", command=convertir_f_a_c, #Uso el command para llamar a la funcion que realiza la conversion
bg="lightgreen", font=("Arial", 10, "bold"), width=12)
boton2.pack(side=tk.LEFT, padx=5)

label_resultado = tk.Label(ventana, text="", bg="gold", font=("Arial", 12, "bold"))
label_resultado.pack(pady=10)#Se crea el label donde se mostrara el resultado de la conversion

# Etiqueta informativa para guiar al usuario
label_info = tk.Label(ventana, text="Ingresa la temperatura y elige la conversión", 
bg="gold", fg="gray", font=("Arial", 9))
label_info.pack(pady=5)#

ventana.mainloop()