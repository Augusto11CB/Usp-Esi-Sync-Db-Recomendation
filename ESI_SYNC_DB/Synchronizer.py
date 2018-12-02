from JsonInsertioDeletionChange import *
from EduBD import *
from time import *
from ESI_WRF.Interface import Interface

class Synchronizer:
    def reset_log(self):
        with open("the_last_logid.txt", "w", encoding='utf-8') as f:
            f.write(str(-1))

    def iniciar_laco(self):
        self.reset_log()
        json_control = JsonInsertioDeletionChange()
        bd_connect = EduBD()
        interface = Interface()

        while True:
            old_id_log = json_control.get_last_id_log()
            log = bd_connect.get_current_version(old_id_log)
            print(log != old_id_log)
            if log != old_id_log:
                json_control.insert_dicionarios(log)
            sleep(120)


s = Synchronizer()
s.iniciar_laco()