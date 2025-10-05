#Usamos Tkinter
import tkinter as tk 
def click_boton(numero):                #Definimos la función que se ejecuta cuando se presiona un botón numerico u operador
    actual= entrada.get()              #Obtenemos el texto que ya esta escrito en la caja de entrada
    entrada.delete(0,tk.END)            #Borramos todo el contenido actual de la caja de entrada
    entrada.insert(0,actual+str(numero))  #Insertamos nuevamente el texto anterior + el nuevo numero/operador
    
def borrar():          #Definimos la funcion borrar
    entrada.delete(0,tk.END)    #Borrar tdo el contenido de la caja de texto "entrada"
    
def calcular():     #Definimos la funcion calcular
    try:                       #Intentamos ejecutar el bloque de codigo
        resultado=eval(entrada.get())    #Evalua lo escrito en la caja de texto como operacion matematica
        entrada.delete(0,tk.END)            #Borra el contenido actual de la caja de texto
        entrada.insert(0,str(resultado))    #Inserta el resultado convertido a texto en la caja de texto
    except:                              #Si ocurre un error(por ejemplo:texto no valido)
        entrada.delete(0,tk.END)         #Borra lo que haya en la caja
        entrada.insert(0,"Error")             #Muestra la palabra "error" en la caja de texto
        
ventana=tk.Tk()
ventana.title("Calculadores con tkinter")
ventana.geometry("300*400")

entrada=tk.Entry(ventana,width=20, font=("Arial",18))

botones= [
    ("7",1.0),("8",1,1),("9",1,2),("/",1,3)
    ("4",2,0),("5",2,1),("6",2,2),("*",2,3)
]
ventana.mainloop()