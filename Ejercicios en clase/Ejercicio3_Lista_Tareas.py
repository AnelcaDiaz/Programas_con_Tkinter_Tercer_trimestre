import tkinter as Tk 
print("Programa de lista de tareas")
ventana = Tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x400")

def agregar_tarea():
    tarea = tarea_entry.get()
    if tarea:
        lista_tareas.insert(Tk.END, tarea)#Agrega la tarea al final de la lista
        tarea_entry.delete(0, Tk.END)#Limpia la caja de texto despues de agregar la tarea
    else:
        print("No se puede agregar una tarea vacía")

def eliminar_tarea():
    try:
        seleccion = lista_tareas.curselection()#El metodo curselection() devuelve una tupla con los índices de los elementos seleccionados
        if seleccion:
            lista_tareas.delete(seleccion) #Elimina la tarea seleccionada
        else:
            print("Selecciona una tarea para eliminar primero") 
    except:
        print("Error al eliminar la tarea")

label_instruccion_entrada = Tk.Label(ventana, text="Escribe tu tarea aquí:")#Etiqueta que indica donde va la caja de texto
label_instruccion_entrada.pack(pady=(10, 0))

# Caja de texto para escribir tareas
tarea_entry = Tk.Entry(ventana, width=30)
tarea_entry.pack(pady=10)

# Botón 'Agregar' para añadir tareas a la lista
agregar_boton = Tk.Button(ventana, text="Agregar", command=agregar_tarea)
agregar_boton.pack(pady=5)

#Es una etiqueta que indica donde van las tareas
label_instruccion_lista = Tk.Label(ventana, text="Tus tareas:")
label_instruccion_lista.pack(pady=(10, 0))
# Listbox para mostrar las tareas
lista_tareas = Tk.Listbox(ventana, width=40, height=10)
lista_tareas.pack(pady=10)

# Botón 'Eliminar' para borrar las tareas seleccionadas
eliminar_boton = Tk.Button(ventana, text="Eliminar", command=eliminar_tarea)
eliminar_boton.pack(pady=5)

ventana.mainloop()