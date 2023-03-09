#Daniel Lopez Mendoza 
#09/03/23

from tkinter import *
from tkinter import ttk

raiz=Tk()
etqTexto=ttk.Label(raiz,text="Join us")
etqTexto.grid()

imagen=PhotoImage(file="d3.png")
imagen2=PhotoImage(file="d1.png")

etqImagen=ttk.Label(raiz)
etqImagen.grid()
etqImagen['image']=imagen

etqCombindada=ttk.Label(raiz, text="We'r see you",compound="bottom")
etqCombindada.grid()
etqCombindada['image']=imagen2

raiz.mainloop()