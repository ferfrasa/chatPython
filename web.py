# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 21:20:59 2019

@author: user
"""


from flask import Flask,render_template,request, json
import mysql.connector as mysql
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


ORIGEN="localhost"
USUARIO="root"
CONTRASENA="****"
BASEDATOS="chat_python"
objetoChat=""


bd= mysql.connect(host=ORIGEN, user=USUARIO, passwd=CONTRASENA, db= BASEDATOS)
cursor= bd.cursor()

app = Flask(__name__)

@app.route("/")
def hello():
 objetoChat=consultarChat()
 print("valores")

 #print(valores)
 return render_template('index.html',consulta=objetoChat,mensaje='')

@app.route("/correo", methods=['GET'])
def eviarCorreo():
    correoElectronico=request.args.get('corre-e')
    MSG=MIMEMultipart()
    mensaje=consultarChat()
    
    password= "*****"
    MSG['From']="tucorreo@correo.com"
    MSG['To']=correoElectronico
    MSG['Subject']="Lista de Chat página Web"
    MSG.attach(MIMEText(str(mensaje),'plain'))

    try:
        
        server = smtplib.SMTP('smtp.gmail.com', port=587)
        server.starttls()
    
        """Ingrese al servicio """
        server.login(MSG['From'],password)
        
        """Enviar el mensaje"""
        server.sendmail(MSG['From'], MSG['To'], MSG.as_string())
        server.quit()
        print("Mensaje enviado a : s%"+ (MSG['To']))
        return render_template('index.html',mensaje='si',consulta=mensaje)
    except Exception:

        return render_template('index.html',mensaje='no',consulta=mensaje)
    

def consultarChat():
 cursor.execute("SELECT * FROM registro_chat")
 chats = cursor.fetchall()
 for row in cursor:
     print(row)
     #valores.join(str(row))
 return chats
     
   

if __name__ == "__main__":

 app.run()
 bd.close() 