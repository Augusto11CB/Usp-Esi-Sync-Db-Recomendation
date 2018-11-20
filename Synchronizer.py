from JsonInsertioDeletionChange import *
from EduBD import *
from time import *


class Synchronizer:
    def __init__(self):
        json_control = JsonInsertioDeletionChange()
        bd_connect = EduBD()

    def iniciar_laco(self):
        while True:
            log_search = bd_connect.get_current_version(json_control.get_last_id_log())
            json_control.insert_dicionarios(log_search)
            sleep(120)

s = Synchronizer()
s.iniciar_laco()