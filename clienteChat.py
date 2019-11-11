# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 15:59:42 2019

@author: user
"""

from tkinter import *
import socket
import threading

root = Tk()  
root.title("Chat del cliente")
root.geometry("500x400")
miFrame= Frame(root, width=500, height=400)
miFrame.pack()
textRespuesta2= Text(miFrame, height=10, width=60)


def pintarInterfaz():

        def enviarMensaje():
            inputValue=textRespuesta.get("1.0","end-1c")
            print(inputValue)
            paquete = inputValue.encode()
           # obSocket.recv(1024):
            obSocket.send(paquete)
            #respuesta=obSocket.recv(1024) 
            #texto= respuesta.decode("utf-8")

            #obSocket.close()

            #textRespuesta2.insert("1.0",texto+"\n")
            textRespuesta.delete("1.0","end-1c")
            
            
       
        miLabel2= Label(miFrame, text="Sala de Chat")
        miLabel2.pack()
        
       # textRespuesta2= Text(miFrame, height=10, width=60)
        scroll= Scrollbar(miFrame, command=textRespuesta2.yview)
        textRespuesta2.configure(yscrollcommand= scroll.set)
        textRespuesta2.pack()
        scroll.pack(side=RIGHT, fill=Y)
        miLabel= Label(miFrame, text="Escribe algo")
        #miLabel.grid(row=0, column=1)
        miLabel.pack()
        textRespuesta= Text(miFrame, height=4, width=30)
        scroll= Scrollbar(miFrame, command=textRespuesta.yview)
        textRespuesta.configure(yscrollcommand= scroll.set)
        textRespuesta.pack()
        scroll.pack(side=RIGHT, fill=Y)

        btEnviar= Button(root, text="Enviar", command=enviarMensaje)
        btEnviar.pack()
        root.mainloop()
        
        


def recibirMensaje():
    while True:
       print("recibio mensaje")
       respuesta=obSocket.recv(1024) 
       texto= respuesta.decode("utf-8")
       textRespuesta2.insert("1.0",texto+"\n")
      

            #obSocket.close()

if __name__ == "__main__":
    print('Ejecutando como programa principal')
    
    obSocket = socket.socket()
    obSocket.connect(('192.168.43.41',8000))
    hilo= threading.Thread(target=recibirMensaje)
    hilo.daemon = True
    hilo.start()
    pintarInterfaz()
    







