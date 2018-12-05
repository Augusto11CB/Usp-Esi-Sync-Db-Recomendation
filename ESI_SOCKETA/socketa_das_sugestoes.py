import socket
from time import*
from threading import Thread
import sys
sys.path.insert(0, '/home/ubuntu/Documents/ESI_SYNC_DB_RECOMENDATION/ESI_SOCKETA/ESI_WRF')
from Interface import Interface


def converter(lista_de_id):
    string_de_ids = ""
    for id in lista_de_id:
        string_de_ids = string_de_ids + "," + id
    return string_de_ids

def threadJob(con):
    myInterface = Interface()
    recebe = con.recv (1024)
    stringincomleta = recebe.decode('latin_1')
    print("sugestão solicitada:"+stringincomleta)
    resposta=myInterface.retorne_sugestoes(stringincomleta)
    print("orignal do wesley:"+str(resposta))
    respostaFinal=str(resposta)
    con.send((respostaFinal+"\n").encode())


cont=0;
while True :
    host = ''
    port = 7300+cont
    addr = (host, port)
    serv_socket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.setsockopt (socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv_socket.bind (addr)
    serv_socket.listen (0)
    con, cliente = serv_socket.accept ()
    serv_socket.close ()
    cont+=1
    if cont==11:
        cont=0
    Thread (target=threadJob, args=[con]).start()
    print("thread DELEGADA")
