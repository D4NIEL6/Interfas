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
f1.grid(column=0,row=0,padx=10,pady=10)

#Nombre 
ttk.Label(f1, text="Nombre:",padding="0 0 20 20").grid(column=0,row=0,sticky=W)
nom=ttk.Entry(f1,width=25)
nom.grid(column=1,row=0,sticky=W+N)

#A paterno
ttk.Label(f1, text="A Paterno:",padding="0 0 20 20").grid(column=0,row=1,sticky=W)
ap=ttk.Entry(f1,width=25)
ap.grid(column=1,row=1,sticky=W+N)

#A materno 
ttk.Label(f1, text="A Mateno:",padding="0 0 20 20").grid(column=0,row=2,sticky=W)
am=ttk.Entry(f1,width=25)
am.grid(column=1,row=2,sticky=W+N)

#Correo
ttk.Label(f1, text="Correo:",padding="0 0 20 20").grid(column=0,row=3,sticky=W)
c=ttk.Entry(f1,width=25)
c.grid(column=1,row=3,sticky=W+N)

#Movil
ttk.Label(f1, text="Movil:",padding="0 0 20 20").grid(column=0,row=4,sticky=W)
m=ttk.Entry(f1,width=25)
m.grid(column=1,row=4,sticky=W+N)

#2do frame
f2=ttk.Frame(struc)
f2.grid(column=1,row=0)

ac=StringVar()
#Bottones
b1=ttk.Radiobutton(f2,text="Estudiante",padding="25 0 0 10",variable=ac,value='b1').grid(column=0,row=0,sticky=W)
b2=ttk.Radiobutton(f2,text="Empleado",padding="25 0 0 10",variable=ac,value='b2').grid(column=0,row=1,sticky=W)
b3=ttk.Radiobutton(f2,text="Desempldeado",padding="25 0 0 10",variable=ac,value='b3').grid(column=0,row=2,sticky=W)

#3er frame
f3=ttk.Frame(struc,padding="30 25 0 10")
f3.grid(column=0,row=1)

af=StringVar()

ttk.Label(f3,text="Aficiones:").grid(column=0,row=0,sticky=W)

cb1=ttk.Checkbutton(f3,text="Leer",padding="0 5 20 0",variable=af,onvalue='Musica'+'Videojuegos').grid(column=0,row=1)
cb2=ttk.Checkbutton(f3,text="Musica",padding="0 5 20 0",variable=af,onvalue='Leer'+'Videojuegos').grid(column=1,row=1)
cb3=ttk.Checkbutton(f3,text="Videojuegos",padding="0 5 20 0",variable=af,onvalue='Leer'+'Musica').grid(column=2,row=1)

#struct 
estado=StringVar
es=ttk.Combobox(struc,textvariable=estado)
es.grid(column=1,row=1)
es['values']=("Jalisco", "Nayarit", "Colima", "Michocan")


#5to frame
f5=ttk.Frame(struc)
f5.grid(column=0,row=2)
b1=ttk.Button(f5,text="Guardar",).grid(column=0,row=0)
b2=ttk.Button(f5,text="Cancelar").grid(column=1,row=0)


rut.mainloop()