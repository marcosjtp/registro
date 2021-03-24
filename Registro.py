###!/usr/bin/env python3.7
import tkinter
from tkinter import*
from tkinter import Tk,messagebox,ttk
#import pymysql
import sqlite3
import os
from os import remove
root=tkinter.Tk()
def SalirApp():
    # check if saving
    # if not:
    sali=messagebox.askquestion("Cerrar","Realmente Deseas serrar la Aplicacion")
    if sali == "yes":
        remove("./fileclose.txt")    
        command=root.destroy() 
root.protocol('WM_DELETE_WINDOW', SalirApp)  # root is your root window  

root.geometry("520x380+360+100")
root.resizable(width=False,height=False)
root.title("Registro")
if os.path.isfile('./fileclose.txt'):
    messagebox.showwarning("informacion",'ya existe una instancia de esta aplicacion \nen caso de no ser asi vaya a la carpeta de intalacion y elimine el archivo (fileclose.txt)')
    command=root.destroy()
else:
    fileser=open("./fileclose.txt","w")
    fileser.write("RegEst esta en ejecucion por favor no borre este archivo\neste evita que existan varias instancia de la aplicacion se \ncrea al iniciar y se elimina al cerrar")   
    fileser.close()
#:::::::::::::::::::::::::::aqui empiezan las variables::::::::::::::::::::::::::::::::::::::::::::::
cursores=["arrow","circle","clock","cross","dotbox","exchange","fleur","heart","heart","man","mouse","pirate","plus","shuttle","sizing","spider","spraycan","star","target","tcross","trek","watch"]
VariableId=StringVar()
VarNombre=StringVar()
VarApellido=StringVar()
VarCedula=StringVar()
VarTelefono=StringVar()
VarDireccion=StringVar()
VarEmail=StringVar()
VarFechaNac=StringVar()
VarCursos=StringVar()
VarServidor=StringVar()
VarContrasena=StringVar()
VarUser=StringVar()
def Primerasconeciones ():
        try:
                #miconeccion=pymysql.Connection(host=VarServidor.get(),user=VarUser.get(),password=VarContrasena.get(),db="mysql")
                #micursor=miconeccion.cursor()
                miconeccion=sqlite3.connect("DataPrincipal")
                micursor=miconeccion.cursor()
                messagebox.showinfo("mensaje","La Conexion con el servidor ha sido exitosa ")
        except :
                messagebox.showinfo("mensaje","La Conexion con el servidor ha Fallado ")
        try:
                micursor.execute("CREATE TABLE IF NOT EXISTS tblestudiantes ( Id_Estudiante INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , Nom_Estudiante VARCHAR(30) NOT NULL, Ape_Estudiante VARCHAR(30), Ced_Estudiante VARCHAR(11) NOT NULL UNIQUE, Tel_Estudiante VARCHAR(10) UNIQUE, Dir_Estudiante VARCHAR(50),Email_Estudiante VARCHAR(50) UNIQUE,Fec_Nac_Estudiante DATE NOT NULL, Cursos_Estudiante VARCHAR(100) )")
                messagebox.showinfo("mensaje","La Tabla tblestudiantes se ha creado correctamente")
                miconeccion.commit()
                miconeccion.close()
        except:
                messagebox.showinfo("mensaje","Por favor revise si la base de dato dataprincipal\n y la Tabla tblestudiantes ya Existe ")
def Func_Guardar():
        try:
                miconeccion=sqlite3.connect("DataPrincipal")
                micursor=miconeccion.cursor()
                #:::::::::::::::::::::::::::::::validando Cedula ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                if len(VarCedula.get())!=11 or VarCedula.get().isdigit()==False:
                        messagebox.showwarning("Error numero de Cedula ","La Cedula es invalida\nEl Formato debe ser sin separacion \"00000000000\" ")
                        TxtCedula.focus()
                        return 0                
                #:::::::::::::::::::::::::::::::Validando Telefono::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                if TxtTelefono.get().isdigit() == False:
                        messagebox.showwarning("ERROR DE CARACTERES","NUMERO DE TELEFONO INVALIDO \nEL # DE TELEFONO SOLO ACEPTA NUMEROS")
                        TxtTelefono.focus()
                        return 0
                if len(VarTelefono.get())!=10 or "-" in VarTelefono.get():
                        messagebox.showwarning("Error Longitud # de  Telefono ","El # de Telefono es invalido\nEl Formato debe ser sin separacion \"0000000000\" ")
                if "@" not in VarEmail.get()or "@" in VarEmail.get()[-1]or "@" in VarEmail.get()[0]or"." not in VarEmail.get()or "." in VarEmail.get()[-1]or "." in VarEmail.get()[0]:
                        messagebox.showwarning("Error de correo","El correo ingresado no es valido\ndebe contener @ y . ")
                        TextEmail.focus()
                msjguar=messagebox.askquestion("Guardar","Realmente Deseas guardar este registro")
                if msjguar == "yes":
                        if VarNombre.get()=="" or VarApellido.get()=="":
                                messagebox.askquestion("Error","Falta informacion!\n Favor Revise  Nombre y Apellido Antes de Continuar") 
                                TxtNombre.focus()
                        micursor.execute("INSERT INTO tblestudiantes VALUES (NULL, ' " + VarNombre.get() +
                        "', '" + VarApellido.get() +
                        "', '" + VarCedula.get() +
                        "', '" + VarTelefono.get() +
                        "', '" + VarDireccion.get() +
                        "', '" + VarEmail.get() +
                        "', '" + VarFechaNac.get() +
                        "','" + TxtCursos.get(1.0, tkinter.END) + "')")
                        messagebox.showinfo("Guardar","Registro guardado con exito")
                        command=funNuevo()
                        miconeccion.commit()
                        miconeccion.close()
        except:
                messagebox.showinfo("Error","El registro no pudo ser guardado revise la informacion suministada e intentelo de nuevo")
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def Actualizar_Registro():
    try:

        #miconeccion=sqlite3.connect("DataPrincipal")
        # micursor= miconeccion.cursor()
        miconeccion=sqlite3.connect("DataPrincipal")
        micursor=miconeccion.cursor()
        #:::::::::::::::::::::::::::::::validando Cedula ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        if TxtCedula.get().isdigit() == False:
                messagebox.showinfo("ERROR DE CARACTERES","EL # DE TELEFONO SOLO ACEPTA NUMEROS")
        if len(VarCedula.get())!=11 or "-" in VarCedula.get():
                messagebox.showinfo("Error Longitud de Cedula ","La Cedula es invalida\nEl Formato debe ser sin separacion \"00000000000\" ")
                return
        #:::::::::::::::::::::::::::::::Validando Telefono::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        if len(VarTelefono.get())!=10 or "-" in VarTelefono.get():
                messagebox.showinfo("Error Longitud # de  Telefono ","El # de Telefono es invalido\nEl Formato debe ser sin separacion \"0000000000\" ")
                return
        if "@" not in VarEmail.get()or "@" in VarEmail.get()[-1]or "@" in VarEmail.get()[0]or"." not in VarEmail.get()or "." in VarEmail.get()[-1]or "." in VarEmail.get()[0]:
                messagebox.showinfo("Error de correo","El correo ingresado no es valido\ndebe contener @ y . ")
                return
        micursor.execute("UPDATE TblEstudiantes SET Nom_Estudiante='" + VarNombre.get() +
            "',Ape_Estudiante='" + VarApellido.get() +
            "',Ced_Estudiante='" + VarCedula.get() +
            "',Tel_Estudiante='" + VarTelefono.get() +
            "',Dir_Estudiante='" + VarDireccion.get() +
            "',Email_Estudiante='" + VarEmail.get() +
            "',Fec_Nac_Estudiante='" + VarFechaNac.get() +
             "',Cursos_Estudiante='" + TxtCursos.get("1.0", tkinter.END) +
            "' WHERE Id_Estudiante=" + VariableId.get())
        messagebox.showinfo("Guardar","Registro Actualizado con exito")
        command=funNuevo()
        miconeccion.commit()
        miconeccion.close()
    except:
            messagebox.showinfo("Error","El registro no pudo ser Actualizado revise la informacion \nsuministada e intentelo de nuevo")
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def Func_Delete():
    try:
        miconeccion=sqlite3.connect("DataPrincipal")
        micursor=miconeccion.cursor()
        msjdel=messagebox.askquestion("Delete","Realmente Deseas Eliminar este registro")
        if msjdel == "yes":
            micursor.execute("DELETE FROM `tblestudiantes` WHERE `tblestudiantes`.`Id_Estudiante` = " + VariableId.get())
            messagebox.showinfo("informacion","El Registro se ha Eliminado con exito")
            miconeccion.commit()
            miconeccion.close()
    except:
        messagebox.showinfo("informacion","Se Produjo un Error Eliminado el Registro")
    command=funNuevo()
def SalirApp ():
    sali=messagebox.askquestion("Cerrar","Realmente Deseas serrar la Aplicacion")
    if sali == "yes":
        remove("./fileclose.txt")    
        command=root.destroy()     
def funNuevo():
        try:
            VariableId.set("")
            VarNombre.set("")
            VarApellido.set("")
            VarCedula.set("")
            VarTelefono.set("")
            VarDireccion.set("")
            VarEmail.set("")
            VarFechaNac.set("")
            TxtCursos.delete(1.0, tkinter.END)
            TxtNombre.focus()
        except:
            messagebox.showinfo("Error","No se ha encontrado que Limpiar")
def msjinfo():
    messagebox.showinfo("informacion", "name=Registro\nVersion=1.0\nDescription=Programa de manipulacion de datos\nAuthor=Marcos Toribio\nauthor_email=marcos.jtp@outlook.com\nurl=mjcomputos.wordpress.com\nCreado en Python 3.7 \n")
def busquedaxcodigo():
    try:
       
        miconeccion=sqlite3.connect("DataPrincipal")
        micursor=miconeccion.cursor()
        micursor.execute("SELECT * FROM tblestudiantes WHERE Id_Estudiante=" + VariableId.get())
        EstudLeido=micursor.fetchall()
        miconeccion.commit()
        miconeccion.close()
        for estudiant in EstudLeido:
            TxtCursos.delete(1.0, tkinter.END)
            VariableId.set(estudiant[0])
            VarNombre.set(estudiant[1])
            VarApellido.set(estudiant[2])
            VarCedula.set(estudiant[3])
            VarTelefono.set(estudiant[4])
            VarDireccion.set(estudiant[5])
            VarEmail.set(estudiant[6])
            VarFechaNac.set(estudiant[7])
            TxtCursos.insert(1.0,estudiant[8])
    except:
        messagebox.showinfo("Error Lectura","No se  ha podido leer el registro ")
def busquedaxcedula():
    try:
       
        miconeccion=sqlite3.connect("DataPrincipal")
        micursor=miconeccion.cursor()
        micursor.execute("SELECT* FROM tblestudiantes WHERE Ced_Estudiante ="+ VarCedula.get() )
        EstudLeido = micursor.fetchall()
        miconeccion.commit()
        miconeccion.close()
        VariableId.set(list(EstudLeido)[0][0])
        command = busquedaxcodigo()
    except:
            messagebox.showinfo("Error Lectura Cedula","No se  ha podido leer el registro ")
def busquedaxtelefono():
    try:
        miconeccion=sqlite3.connect("DataPrincipal")
        micursor=miconeccion.cursor()
        micursor.execute("SELECT* FROM tblestudiantes WHERE Tel_Estudiante=" + VarTelefono.get())
        EstudLeido = micursor.fetchall()
        miconeccion.commit()
        miconeccion.close()
        VariableId.set(list(EstudLeido)[0][0])
        command = busquedaxcodigo()
    except:
            messagebox.showinfo("Error Lectura Cedula","No se  ha podido leer el registro ")
def busquedaxemail():
    try:
        miconeccion=sqlite3.connect("DataPrincipal")
        micursor=miconeccion.cursor()
        micursor.execute("SELECT Id_Estudiante FROM tblestudiantes WHERE Email_Estudiante = '" + VarEmail.get()+ "' ORDER BY Id_Estudiante")
        EstudLeido = micursor.fetchall()
        miconeccion.commit()
        miconeccion.close()
        VariableId.set(list(EstudLeido)[0][0])
        command=busquedaxcodigo()

    except:
        messagebox.showinfo("Error Lectura de Email","No se  ha podido leer el registro ")
def FunUltimoRegistro():
        try:
                miconeccion=sqlite3.connect("DataPrincipal")
                micursor=miconeccion.cursor()
                micursor.execute("SELECT * FROM tblestudiantes  Id_Estudiante ORDER BY Id_Estudiante DESC")#ASC
                EstudLeido=micursor.fetchall()
                miconeccion.commit()
                miconeccion.close()
                VariableId.set(EstudLeido[0][0])
                command=busquedaxcodigo()
        except:
                messagebox.showinfo("Error","parece que ya estas en el ultimo registro\no no se ha conectado a la base datos")
def FunPrimerRegistro():
        try:
                miconeccion=sqlite3.connect("DataPrincipal")
                micursor=miconeccion.cursor()
                micursor.execute("SELECT * FROM tblestudiantes  Id_Estudiante ORDER BY Id_Estudiante ASC")#ASC
                EstudLeido=micursor.fetchall()
                miconeccion.commit()
                miconeccion.close()
                VariableId.set(EstudLeido[0][0])
                command=busquedaxcodigo()
        except:
                messagebox.showinfo("Error","parece que ya estas en el Primer registro\no no se ha conectado a la base datos")
def funAnterior():
        try:
                miconeccion=sqlite3.connect("DataPrincipal")
                micursor=miconeccion.cursor()
                micursor.execute("SELECT Id_Estudiante FROM tblestudiantes ORDER BY Id_Estudiante ASC")#DESC
                EstudLeid=micursor.fetchall()
                miconeccion.commit()
                miconeccion.close()
                sumador=VariableId.get()
                sumador2=int(sumador)
                act=EstudLeid[1][0]
                if sumador2 >= act:
                        sumador2-=1
                        VariableId.set(sumador2)
                        command=busquedaxcodigo()
                elif sumador2 <= act:
                        messagebox.showinfo("Error","Registro No Encontrado\npuede ser que ya estes en el primer registro ")
        except:
                messagebox.showinfo("Error","No Se ha Encontrado Registro")
def funSiguiente():
        try:
                miconeccion=sqlite3.connect("DataPrincipal")
                micursor=miconeccion.cursor()
                micursor.execute("SELECT Id_Estudiante FROM tblestudiantes ORDER BY Id_Estudiante DESC")#DESC
                EstudLeid=micursor.fetchall()
                miconeccion.commit()
                miconeccion.close()
                sumador=VariableId.get()
                sumador2=int(sumador)
                act=EstudLeid[1][0]
                if sumador2 <= act:
                        sumador2+=1
                        VariableId.set(sumador2)
                        command=busquedaxcodigo()
                
                elif sumador2 > act:
                        messagebox.showinfo("Error","Registro No Encontrado \npuede ser que ya estes en el Ultimo registro")
        except:
                messagebox.showinfo("Error","Erro al ir al Siguiente Registro")

#::::::::::::::::::::::::::::::::::::::::Aqui terminan las Funciones ::::::::::::::::::::::::::::::::::::

#:::::::::::::::::::::::::::::::::::::::::omienso Menu desplegable::::::::::::::::::::::::::::::::::::::::::::::     
barraMenu=tkinter.Menu(root,bg="white")
root.config(menu=barraMenu, width=300, height=300, bg="white",cursor="heart")
menuconect=tkinter.Menu(barraMenu, tearoff=0,bg="white",activebackground ="orange")
menuconect.add_command(label="Conectar",command=Primerasconeciones,activebackground ="green")
menuconect.add_command(label="Salir",command=SalirApp,activebackground ="green")
barraMenu.add_cascade(label="Inicio",menu=menuconect,activebackground ="orange")
bbddMenu=tkinter.Menu(barraMenu, tearoff=0,activebackground ="green",bg="white")
bbddMenu.add_command(label="Guardar",command=Func_Guardar,activebackground ="green") 
bbddMenu.add_command(label="Actualizar",command=Actualizar_Registro,activebackground ="green")
bbddMenu.add_command(label="Nuevo",command=funNuevo,activebackground ="green")
bbddMenu.add_command(label="Eliminar",command=Func_Delete,activebackground ="green")
barraMenu.add_cascade(label="Registro",menu=bbddMenu,activebackground ="Orange")

menuventanas=tkinter.Menu(barraMenu, tearoff=0,activebackground ="green",bg="white")
menuventanas.add_command(label="Primero",command=FunPrimerRegistro,activebackground ="green")
menuventanas.add_command(label="Siguiente",command=funSiguiente,activebackground ="green")
menuventanas.add_command(label="Anterior",command=funAnterior,activebackground ="green")
menuventanas.add_command(label="Ultimo",command=FunUltimoRegistro,activebackground ="green")
barraMenu.add_cascade(label="Movimientos",menu=menuventanas,activebackground ="orange")
menubuscar=tkinter.Menu(barraMenu, tearoff=0,activebackground ="green",bg="white")
menubuscar.add_command(label="Por Email", command=busquedaxemail,activebackground ="green")
menubuscar.add_command(label="Por Codigo",command=busquedaxcodigo,activebackground ="green")
menubuscar.add_separator()
menubuscar.add_command(label="Por Cedula",command=busquedaxcedula,activebackground ="green")
menubuscar.add_separator()
menubuscar.add_command(label="Por Telefono",command=busquedaxtelefono,activebackground ="green")
barraMenu.add_cascade(label="Busqueda",menu=menubuscar,activebackground ="orange")
menuinfo=tkinter.Menu(barraMenu, tearoff=0,activebackground ="green",bg="white")
menuinfo.add_command(label="Acerca de...",command=msjinfo,activebackground ="green")
barraMenu.add_cascade(label="Ayuda...",menu=menuinfo,activebackground ="orange")
#::::::::::::::::::::::::::::Aqui termina el menu desplegable:::::::::::::::::::::::::::::::::

#:::::::::::::::::::::::::::Aqui empiezan los cuadros de textos::::::::::::::::::::::::::::::::

#::::::::::::::::::::::::Aqui empiezan los Entry o cajas de texto corto :::::::::::::::::::
TxtNombre=tkinter.Entry(root, textvariable=VarNombre, width=25)
TxtNombre.grid(row=1,column=1,padx=10,sticky="w")
TxtNombre.config(bg="white")
TxtNombre.focus()
TxtApellido=tkinter.Entry(root, textvariable=VarApellido, width=25)
TxtApellido.grid(row=2,column=1,padx=10,sticky="w")
TxtApellido.config(bg="white")
TxtCedula=tkinter.Entry(root, textvariable=VarCedula, width=11)
TxtCedula.grid(row=3,column=1,padx=10,sticky="w")
TxtCedula.config(bg="white")
TxtTelefono=tkinter.Entry(root, textvariable=VarTelefono, width=10)
TxtTelefono.grid(row=4,column=1,padx=10,sticky="w")
TxtTelefono.config(bg="white")
TxtDireccion=tkinter.Entry(root, width=50, textvariable=VarDireccion)
TxtDireccion.grid(row=5,column=1,padx=10,sticky="w",columnspan=3)
TxtDireccion.config(bg="white")
TextEmail=tkinter.Entry(root, width=50, textvariable=VarEmail)
TextEmail.grid(row=6,column=1,padx=10,sticky="w",columnspan=3)
TextEmail.config(bg="white")
TxtFechaNac=tkinter.Entry(root, textvariable=VarFechaNac, width=10)
TxtFechaNac.grid(row=7,column=1,padx=10,sticky="w")
TxtFechaNac.config(bg="white")
TxtCursos=tkinter.Text(root)
TxtCursos.grid(row=8,column=1,padx=10,sticky="w")
TxtCursos.config(bg="white",width=20,height=4)
TxtId=tkinter.Entry(root, textvariable=VariableId,width=11)
TxtId.grid(row=0, column=1, padx=10, sticky="w")
TxtId.config(bg="white")
"""
ComboUser =ttk.Combobox(root,textvariable=VarUser,width=15,justify="right")
ComboUser.grid(row=3,column=6,sticky="e")
ComboUser["values"]=("root","admin")
ComboUser.current(0)
#:::::::::::::::::empieza la configuracion del campo servidor:::::::::::::::::::::::::::::::::
tupleserver=open("servidole.txt","r")
serv=tupleserver.read()
tupleserver.close()
ComboServer =ttk.Combobox(root,textvariable=VarServidor,width=15,justify="right")
ComboServer.grid(row=1,column=6,sticky="e")
ComboServer["values"]=(serv)
ComboServer.current(0)#valor predeterminado del Combobox (primera posicion )
#:::::::::::::::::Termina la configuracion del campo servidor:::::::::::::::::::::::::::::::::
TxtPassword=tkinter.Entry(root, textvariable=VarContrasena,width=15,show="*",justify="right")
TxtPassword.grid(row=5,column=6,sticky="e")
TxtPassword.config(bg="white",)"""
#::::::::::::::::::::::::::Aqui empiezan los Botton:::::::::::::::::::::::::::::::::::::::::::
miframe=tkinter.Frame(root, cursor="trek")
miframe.grid(row=10,column=1,columnspan=7)
miframe.config(bg="white",)
#imagenes Botones
imgguardar=PhotoImage(file="./Save.png")
imgActualizar=PhotoImage(file="./Actualizar.png")
imgEliminar=PhotoImage(file="./Eliminar.png")
imgNuevo=PhotoImage(file="./Nuevo.png")
imgprimero=PhotoImage(file="./primero.png")
imganterior=PhotoImage(file="./anterior.png")
imgsiguiente=PhotoImage(file="./siguiente.png")
imgultimo=PhotoImage(file="./ultimo.png")
#fin imagen botones 
root.wm_attributes("-topmost", 0)
btnGuardar=Button(miframe,text="Guardar",command=Func_Guardar,image=imgguardar,width=100,height=30,bg="white", takefocus=funNuevo,relief=FLAT, activebackground ="green",
       background ="white")#.place(x=100,y=100)#desde aqui empieza el diseno Larg    o de los botones
btnGuardar.grid(row=0,column=0,padx=2,pady=10)
btnActualizar=Button(miframe,text="Actualizar",command=Actualizar_Registro,image=imgActualizar,width=100,height=30,bg="white",activebackground ="green")
btnActualizar.grid(row=0,column=1,padx=2,pady=10)
#btnBuscar=ttk.Button(miframe,text="Buscar",command=busquedaxcodigo).grid(row=0,column=3,padx=3)#desde aqui empieza el diseno corto de los botones
btnNuevo=Button(miframe,text="Nuevo",command=funNuevo,image=imgNuevo,width=100,height=30,bg="white",activebackground ="green").grid(row=0,column=3,padx=2)
btnEliminar=Button(miframe,text="Eliminar",command=Func_Delete,image=imgEliminar,width=100,height=30,bg="white",activebackground ="green").grid(row=0,column=4,padx=2)
#btnsalir=ttk.Button(miframe,text="Salir",command=SalirApp).grid(row=0,column=6,padx=3)
miframemovimiento=tkinter.Frame(root,bg="white")
miframemovimiento.grid(row=0,column=2,sticky="e")
btnSiguiente=Button(miframemovimiento,text=">",command=funSiguiente,image=imgsiguiente,width=40,height=30,bg="white",activebackground ="green").grid(row=0,column=2,padx=3)
btnAnterior=Button(miframemovimiento,text="<",command=funAnterior,image=imganterior,width=40,height=30,bg="white",activebackground ="green").grid(row=0,column=1,padx=3)
btnPrimero=Button(miframemovimiento,text="<<",command=FunPrimerRegistro,image=imgprimero,width=40,height=30,bg="white",activebackground ="green").grid(row=0,column=0,padx=3)
btnUltimo =Button(miframemovimiento, text=">>", command=FunUltimoRegistro,image=imgultimo,width=40,height=30,bg="white",activebackground ="green").grid(row=0, column=3, padx=3)
#::::::::::::::::::::::::::aqui empiezan los label::::::::::::::::::::::::::::::::::::::::::::::
LbId=tkinter.Label(root, text="CODIGO")
LbId.grid(row=0,column=0,pady=5,sticky="e")
LbId.config(bg="white")
LbNombre=tkinter.Label(root, text="NOMBRE")
LbNombre.grid(row=1,column=0,pady=5,sticky="e")
LbNombre.config(bg="white")
LbApellido=tkinter.Label(root, text="APELLIDO")
LbApellido.grid(row=2,column=0,pady=5,sticky="e")
LbApellido.config(bg="white")
LbCedula=tkinter.Label(root, text="CEDULA")
LbCedula.grid(row=3,column=0,pady=5,sticky="e")
LbCedula.config(bg="white")
LbTelefono=tkinter.Label(root, text="TELEFONO")
LbTelefono.grid(row=4,column=0,pady=5,sticky="e")
LbTelefono.config(bg="white")
LbDireccion=tkinter.Label(root, text="DIRECCION")
LbDireccion.grid(row=5,column=0,pady=5,sticky="e")
LbDireccion.config(bg="white")
LbEmail=tkinter.Label(root, text="EMAIL")
LbEmail.grid(row=6,column=0,pady=5,sticky="e")
LbEmail.config(bg="white")
LbFechNac=tkinter.Label(root, text="FECHA NAC")
LbFechNac.grid(row=7,column=0,pady=5,sticky="e")
LbFechNac.config(bg="white")
LbCursos=tkinter.Label(root, text="CURSOS")
LbCursos.grid(row=8,column=0,pady=5,sticky="e")
LbCursos.config(bg="white")

"""LbServer=tkinter.Label(root, text="SERVER")
LbServer.grid(row=0,column=6,pady=0,sticky="e")
LbServer.config(bg="white")
LbUser=tkinter.Label(root, text="User")
LbUser.grid(row=2,column=6,pady=0,sticky="e")
LbUser.config(bg="white")
LbPassword=tkinter.Label(root, text="PASSWORD")
LbPassword.grid(row=4,column=6,pady=0,sticky="e")
LbPassword.config(bg="white")"""
#:::::::funcion que inicia  la Aplicacion :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
root.mainloop()
#::::::::::::::::::::::::::::::

