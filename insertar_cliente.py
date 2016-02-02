# -*- coding: utf-8 -*-
import mysql.connector
from mysql.connector import Error
from Tkinter import *
from mysql.connector import errorcode
__author__ = 'cgrulo'

ventana = Tk()
ventana.title('Insertar Cliente')

# -----------------------------------------Funciones------------------------------------------------------


def ingresar():
    cop = int(cp.get())
    base_datos(nombre.get(), paterno.get(), materno.get(), deleg.get(), cop, direccion.get(), fecha.get(), mail.get())


# -------------------------Conexion con la base de datos----------------------------


def base_datos (nombre, paterno, materno, deleg, cp, direccion, fecha, mail):
    try:
        database = mysql.connector.connect(host='localhost',
                                           database='erp_jaque',
                                           user='root',
                                           password='UnoDosTres')

        if database.is_connected():
            print 'Conexion establecida'

            cursor = database.cursor()

            # Comando SQL

            query = "insert into cliente (nom_cli, apep_cli, apem_cli, fecha_cli, del_cli, cp_cli, dir_cli ,mail_cli)" \
                    " values(%s,%s,%s,%s,%s,%s,%s,%s) "

            # Valores a enviar en el comando

            args = (nombre, paterno, materno, fecha, deleg, cp, direccion, mail)

            cursor.execute(query, args)
            print 'Se ingresaron datos'
            # print nombre + paterno + materno + fecha + deleg + cp + direccion + mail

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    finally:

        cursor.close()
        database.close()

# --------------------------------------------Texto de la ventana------------------------------------------

etiqueta1 = Label(ventana, text='Nombre:').grid(row=0, column=0)
etiqueta2 = Label(ventana, text='Apellido Paterno::').grid(row=1, column=0)
etiqueta3 = Label(ventana, text='Apellido Materno:').grid(row=2, column=0)
etiqueta4 = Label(ventana, text='Delegacion:').grid(row=3, column=0)
etiqueta5 = Label(ventana, text='Codigo Postal:').grid(row=4, column=0)
etiqueta6 = Label(ventana, text='Direccion:').grid(row=5, column=0)
etiqueta7 = Label(ventana, text='Fecha:').grid(row=6, column=0)
etiqueta8 = Label(ventana, text='Mail:').grid(row=7, column=0)
# --------------------------------------Variables de las entradas------------------------------------------

nombre = StringVar()
paterno = StringVar()
materno = StringVar()
deleg = StringVar()
cp = IntVar()
direccion = StringVar()
fecha = StringVar()
mail =StringVar()
# -------------------------------------------Cuadros de entrada de la ventana------------------------------

ent_nombre = Entry(ventana, textvariable=nombre).grid(row=0, column=1)
ent_paterno = Entry(ventana, textvariable=paterno).grid(row=1, column=1)
ent_materno = Entry(ventana, textvariable=materno).grid(row=2, column=1)
ent_deleg = Entry(ventana, textvariable=deleg).grid(row=3, column=1)
ent_cp = Entry(ventana, textvariable=cp).grid(row=4, column=1)
ent_dir = Entry(ventana, textvariable=direccion).grid(row=5, column=1)
ent_fecha = Entry(ventana, textvariable=fecha).grid(row=6, column=1)
ent_mail = Entry(ventana, textvariable=mail).grid(row=7, column=1)

# --------------------------------------------Boton para ingresar datos-------------------------------------

boton = Button(ventana, text='Ingresar', command=ingresar).grid(row=8, column=1)

ventana.mainloop()
