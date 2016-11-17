#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys 

# Cliente UDP simple.

# Dirección IP del servidor.


INFO = sys.argv[2]
INFO1 = INFO.split("@")
INFO2 = INFO1[1].split(":")


PORT = int(INFO2[1])
SERVER = (INFO2[0])
USER = (INFO1[0])


print("ESTAS SON LAS VARIABLES QUE ME DAN:")
print("Este es el servidor: " , SERVER)
print("Este es el puerto: " , PORT)
print("Este es el usuario: " , USER)


REQUEST = sys.argv[1]


if len(sys.argv) != 3:
    sys.exit("Usage: python client.py method receiver@IP:SIPport")

# Contenido que vamos a enviar

LINE_SIP = " sip:" + USER + "@" + SERVER + " SIP/2.0\r\n\r\n"
LINE = REQUEST + LINE_SIP
#LINE = '¡SOY BATMAN!'

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER,PORT))

print("Enviando: " + LINE)
my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)

print(data.decode('utf-8'))
#[0:-1] Te coge desde el principio hasta el final menos el ultimo
WERECEIVE = data.decode('utf-8').split('\r\n\r\n')[0:-1]


MUSTRECEIVE100 = ("SIP/2.0 100 Trying")
MUSTRECEIVE180 = ("SIP/2.0 180 Ring")
MUSTRECEIVE200 = ("SIP/2.0 200 OK")
MUSTRECEIVE = [MUSTRECEIVE100, MUSTRECEIVE180, MUSTRECEIVE200]


if WERECEIVE == MUSTRECEIVE:
    LINE_ACK = "ACK" + LINE_SIP
    #Linea inventada
    print("Enviando ACK...", LINE_ACK)
    my_socket.send(bytes(LINE_ACK, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    

print('Recibido -- ', WERECEIVE)
print("Terminando socket...")

# Cerramos todo
my_socket.close()
print("Fin.")
