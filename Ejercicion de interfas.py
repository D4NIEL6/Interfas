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

#2do frame
f2=ttk.Frame(struc)
f2.grid(column=1,row=0)

#Bottones
b1=ttk.Radiobutton(f2,text="Estudiante",padding="25 0 0 10").grid(column=0,row=0,sticky=W)
b2=ttk.Radiobutton(f2,text="Empleado",padding="25 0 0 10").grid(column=0,row=1,sticky=W)
b3=ttk.Radiobutton(f2,text="Desempldeado",padding="25 0 0 10").grid(column=0,row=2,sticky=W)

#3er frame
f3=ttk.Frame(struc,padding="30 25 0 10")
f3.grid(column=0,row=1)

ttk.Label(f3,text="Aficiones:").grid(column=0,row=0,sticky=W)

ttk.Checkbutton(f3,text="Leer",padding="0 5 20 0").grid(column=0,row=1)
ttk.Checkbutton(f3,text="Musica",padding="0 5 20 0").grid(column=1,row=1)
ttk.Checkbutton(f3,text="Videojuegos",padding="0 5 20 0").grid(column=2,row=1)
rut.mainloop()