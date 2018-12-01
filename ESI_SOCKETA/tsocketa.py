import socket
from time import*
from threading import Thread
# from Interface import Interface


def converter(lista_de_id):
    string_de_ids = ""
    for id in lista_de_id:
        string_de_ids = string_de_ids + "," + id
    return string_de_ids

def threadJob(con):
    print("Conectou!")
    # myInterface = Interface()
    # recebe = con.recv (1024)
    # numero_de_resultados = recebe.decode()
    # lista_de_id = myInterface.devolveRecomendacaoPaginaInicial(int(numero_de_resultados))
    # string_de_ids = converter(lista_de_id)
    string_de_ids = "{1,2,3,4,5,6,7,8,9,10,11}\n"
    con.send(string_de_ids.encode())



cont=0;
while True :
    host = ''
    port = 7103+cont
    addr = (host, port)
    serv_socket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.setsockopt (socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv_socket.bind (addr)
    serv_socket.listen (5)
    con, cliente = serv_socket.accept ()
    serv_socket.close ()
    cont+=1
    if cont==11:
        cont=0
    Thread (target=threadJob, args=[con]).start()
    print("thread DELEGADA")





