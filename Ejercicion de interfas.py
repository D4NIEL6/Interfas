#Ejercicion de interfas
#Daniel Lopez Mendoza
#09/03/23

from tkinter import*
from tkinter import ttk
 
rut=Tk()

rut.title("Muestra Widnegs")

struc=ttk.Frame(rut,padding="10 10 10 10")
struc.grid(column=0,row=0)

#1er freame 

f1=ttk.Frame(struc,padding="5 5 5 5")
f1.grid(column=0,row=0)

#Nombre 
ttk.Label(f1, text="Nombre:",padding="0 0 20 0").grid(column=0,row=0,sticky=W)
nom=ttk.Entry(f1,width=25)
nom.grid(column=1,row=0)

#A paterno
ttk.Label(f1, text="A Paterno:",padding="0 0 20 0").grid(column=0,row=1,sticky=W)
ap=ttk.Entry(f1,width=25)
ap.grid(column=1,row=1)

#A materno 
ttk.Label(f1, text="A Mateno:",padding="0 0 20 0").grid(column=0,row=2,sticky=W)
am=ttk.Entry(f1,width=25)
am.grid(column=1,row=2)

#Correo
ttk.Label(f1, text="Correo:",padding="0 0 20 0").grid(column=0,row=3,sticky=W)
c=ttk.Entry(f1,width=25)
c.grid(column=1,row=3)

#Movil
ttk.Label(f1, text="Movil:",padding="0 0 20 0").grid(column=0,row=4,sticky=W)
m=ttk.Entry(f1,width=25)
m.grid(column=1,row=4)

rut.mainloop()