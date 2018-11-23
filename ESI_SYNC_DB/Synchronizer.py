from JsonInsertioDeletionChange import *
from EduBD import *
from time import *


class Synchronizer:

    def iniciar_laco(self):
        json_control = JsonInsertioDeletionChange()
        bd_connect = EduBD()
        interface = Interface()

        while True:
            log = bd_connect.get_current_version(json_control.get_last_id_log())
            print(log)
            json_control.insert_dicionarios(log)
            sleep(120)


s = Synchronizer()
s.iniciar_laco()