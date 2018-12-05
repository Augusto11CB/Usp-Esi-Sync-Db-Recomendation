import socket
from time import*
from threading import Thread
from Interface import Interface


def converter(lista_de_id):
    string_de_ids = ""
    for id in lista_de_id:
        string_de_ids = string_de_ids + "," + id
    return string_de_ids

def threadJob(con):
    myInterface = Interface()
    recebe = con.recv (1024)
    numero_de_resultados = recebe.decode()
    print("numero de resultados:"+numero_de_resultados)
    lista_de_id = myInterface.devolveRecomendacaoPaginaInicial(int(numero_de_resultados))
    print("orignal do wesley:"+str(lista_de_id))
    string_de_ids = str(lista_de_id)
    print("respota:"+string_de_ids)
    con.send((string_de_ids+"\n").encode())


cont=0;
while True :
    host = ''
    port = 7100+cont
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





