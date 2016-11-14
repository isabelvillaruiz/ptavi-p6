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


print("Este es el servidor" , SERVER)
print("Este es el puerto" , PORT)

REQUEST = sys.argv[1]


if len(sys.argv) != 3:
    sys.exit("Usage: python client.py method receiver@IP:SIPport")

# Contenido que vamos a enviar
'''
if REQUEST == 'Invite':
    
elif REQUEST == 'Bye':

'''

 


LINE = '¡Hola mundo!'

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER,PORT))

print("Enviando: " + LINE)
my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)

print('Recibido -- ', data.decode('utf-8'))
print("Terminando socket...")

# Cerramos todo
my_socket.close()
print("Fin.")
