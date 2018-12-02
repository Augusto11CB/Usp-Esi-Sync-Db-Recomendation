import smtplib
import sys
import json
sys.path.insert(0, "../ESI_WRF/")
from Interface import Interface

class JsonInsertioDeletionChange():

    dicio_aux = {
            "categoria_log": "VERAO",
            "id_log": 2,
            "id_produto": 0,
            "nome":"camisa",
            "preco": 0,
            "tags_log": [
             "Amarela","Colorida","Florida"
            ],
            "type_log": "ALTERAÇÃO"
    }

    # dic {}
    # list []

    def insert_dicionarios(self, myJson):#myJson == []
        # dic {}
        # list []
        insercoes = []
        atualizacoes = []
        delete_list = []
        #myJson is a list 
        sendAlert = EnviarNotificacao()
        print(1)
        print(myJson)
        myJson = json.loads(myJson)
        print(2)
        print(myJson)
        for dicio in myJson:
            print(dicio["type_log"])
            if str(dicio["type_log"]) is 'INSERT':
                insercoes.append(dicio)
            elif str(dicio["type_log"]) is 'DELETE': #Só id
                delete_list.append(str(dicio["id_produto"]))#lista de ids
            else:
                atualizacoes.append(dicio)

        MyInterface = Interface()
        error = MyInterface.realiza_operacoes_atualizacao_bd(insercoes, atualizacoes, delete_list)
        if error is not None:
            print(error)
            pass
            #sendAlert.enviarEmail(error)
        
        #saving the last value read at or json
        print(len(myJson))
        last_dicio = myJson[-1]
        with open("the_last_logid.txt", "w", encoding='utf-8') as f:

            f.write(str(last_dicio["id_log"]))


    def get_last_id_log(self):
        f = open("the_last_logid.txt","r").read()
        return int(f)

    def __init__(self):
        pass
        



            
class EnviarNotificacao():
    global remetente
    global senha

    def __init__(self) :
        self.remetente = 'caminhopara6milhoes@gmail.com'
        self.senha = 'osu!isjustaclickaway'

    def enviarEmail(self, erro) :

        # Informações da mensagem
        destinatario = ['augusto.bueno@usp.br',
        'augusto.calado11@gmail.com','wesley.ramos.santos@usp.br','rainer.henrique.oliveira@usp.br','gustavo.herique@usp.br']
        assunto      = 'Problema na Atuaizacao do BD'
        texto        = erro
        
        # Preparando a mensagem
        msg = '\r\n'.join([
        'From: %s' % self.remetente,
        'To: %s' % destinatario,
        'Subject: %s' % assunto,
        '',
        '%s' % texto
        ])

        # Enviando o email
        
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(self.remetente, self.senha)
        server.sendmail(self.remetente, destinatario, msg)
        server.close()
