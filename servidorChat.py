# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 19:08:55 2019

@author: user
"""

import mysql.connector as mysql
import socket
import time
import threading



ORIGEN="localhost"
USUARIO="root"
CONTRASENA=""
BASEDATOS="chat_python"
listaSocketCliente=[]
listaDirecciones=[]


bd= mysql.connect(host=ORIGEN, user=USUARIO, passwd=CONTRASENA, db= BASEDATOS)
cursor= bd.cursor()


def enviarMensajeAll (conexion, message):
    
    	for valor in listaSocketCliente:
            print(valor)
            print(message)
            valor.send(message)

def recibirMensajeCliente(conexion, direccion):
    while True:
         mensaje_recibido=conexion.recv(1024) 
         ahora = time.strftime("%c")
         fecha= time.strftime("%c")    
         texto= mensaje_recibido.decode("utf-8")
         comando= "INSERT INTO registro_chat (ip_chat,mensaje_chat,fecha_chat) values(%s,%s,%s);"
         valores= (str(direccion),str(texto),str(ahora))
         cursor.execute(comando,valores)
         bd.commit()
         
         cursor.execute("SELECT * FROM registro_chat")
         for row in cursor:
           print(row)
         valor = len(listaSocketCliente)
         print("valor0", valor)
         enviarMensajeAll(conexion,(str(ahora)+"-"+str(direccion)+"::"+texto).encode())
        
    
    

def operacionChat(conexion, direccion):
    
        print (conexion)
        print (direccion)
        listaSocketCliente.append(conexion)
        listaDirecciones.append(direccion)
        hilo= threading.Thread(target=recibirMensajeCliente, args=(conexion,direccion))
        hilo.daemon = True
        hilo.start()
    
    

   
if __name__ == "__main__":
    print('Ejecutando como programa principal')
    obSocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    obSocket.bind(('192.168.43.41',8000))
    clientes=5
    obSocket.listen(clientes)
    

    while True:
        conexiones=1
    
        for conexiones in range(clientes):
        #aceptar las peticiones de los clientes
            conexion, direccion = obSocket.accept()
            #print("nueva conexion"+ direccion)
           
            hilo= threading.Thread(target=operacionChat, args=(conexion,direccion))
            hilo.daemon = True
            hilo.start()
    bd.close()
    conexiones=1       
    for conexiones in range(clientes):
      listaSocketCliente[conexiones].close()
   

