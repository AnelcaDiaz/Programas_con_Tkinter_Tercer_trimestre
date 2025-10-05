import tkinter
ventana=tkinter.Tk()
ventana.geometry("400x300")

def saludo(nombre):
    print("Bienvenido"+nombre)
#Caja de texto se usa Entry especificando donde va estar mas el método que se llama pack()
cajatexto=tkinter.Entry(ventana)
cajatexto.pack()

etiqueta=tkinter.Label(ventana)
etiqueta.pack()
def textodelacaja():
    text20=cajatexto.get()
    etiqueta["text"]=text20
    print(text20)
    
boton1=tkinter.Button(ventana,text="Presiona", command=saludo)
boton1.pack()

ventana.mainloop()

