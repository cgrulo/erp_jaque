# -*- coding: utf-8 -*-
__author__ = 'cgrulo'

import mysql.connector
from mysql.connector import Error
servidor="host='localhost', database='erp_jaque', user='root', password='UnoDosTres'"

def insertar_cliente(nombre, appaterno, apmaterno, fecha, delecgacion, cpostal, direccion):
    try:
        global servidor
        print 'estableciendo conexion...'

        #Conexion con el seridor
        database=servidor

        if database.is_connected():
            print'Conexion establecida'
            cursor=database.cursor()

            query="insert into cliente(nom_cli,apep_cli,apem_cli,fecha_cli, del_cli, cp_cli, dir_cli)" \
                  " values(%s,%s,%s,%s,%s,%d,%s)"

            args=(nombre, appaterno, apmaterno, fecha, delecgacion, cpostal, direccion)

            cursor.execute(query,args)

            if cursor.lastrowid:
                print('last insert id', cursor.lastrowid)
            else:
                print('last insert id not found')

            database.commit()


    except Error:
        print (Error)

    finally:

        cursor.close()
        database.close()


