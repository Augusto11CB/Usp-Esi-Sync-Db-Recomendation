import socket
from time import*
from threading import Thread

def threadJob(con ):
    recebe = con.recv (1024)
    print ("mensagem recebida: " + recebe.decode ())
    sleep(5);
    con.send (("resposta ao metodo"+recebe.decode()).encode ())


    pass

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





