import socket
from time import *
from decimal import Decimal
from threading import Thread
from Interface import Interface
from Busca import Busca

def converter(lista_de_id):
    string_de_ids = ""
    for id in lista_de_id:
        string_de_ids = string_de_ids + "," + id
    return string_de_ids

def parsear(entrada_url):
    dicio_de_entradas = entrada_url.split(",")
    return dicio_de_entradas

def threadJob(con):
    
    recebe = con.recv (1024)
    entradas_da_url = recebe.decode()
    dicio_de_entradas = parsear(entradas_da_url)

    myInterface = Interface()
    b = Busca()
# b.atribui_ordenacao('preco')
    b.atribui_busca(dicio_de_entradas[0])
    b.atribui_categoria(dicio_de_entradas[1])
    b.atribui_id(int(dicio_de_entradas[2]))
    b.atribui_valor_maximo(Decimal(dicio_de_entradas[3]))
    b.atribui_valor_minimo(Decimal(dicio_de_entradas[4]))

    lista_de_id = myInterface.busque(b)

    string_de_ids = converter(lista_de_id)
    con.send(string_de_ids.encode())

cont=0;
while True :
    host = ''
    port = 7000+cont
    addr = (host, port)
    serv_socket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.setsockopt (socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv_socket.bind (addr)
    serv_socket.listen (0)
    con, cliente = serv_socket.accept ()
    serv_socket.close ()
    cont+=1
    if cont==101:
        cont=0
    Thread (target=threadJob, args=[con]).start()
    print("thread DELEGADA")





