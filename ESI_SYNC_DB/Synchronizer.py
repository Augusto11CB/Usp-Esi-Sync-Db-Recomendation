from JsonInsertioDeletionChange import *
from EduBD import *
from time import *
from ESI_WRF.Interface import Interface
import traceback

class Synchronizer:
    def reset_log(self):
        with open("the_last_logid.txt", "w", encoding='utf-8') as f:
            f.write(str(-1))

    def iniciar_laco(self):
        self.reset_log()
        json_control = JsonInsertioDeletionChange()
        error_handler = EnviarNotificacao()
        bd_connect = EduBD()
        interface = Interface()

        error_number = 0
        while True:
            errorless = True
            try:
                old_id_log = json_control.get_last_id_log()
                log = bd_connect.get_current_version(old_id_log)
                if log != old_id_log:
                    json_control.insert_dicionarios(log)
            except:
                errorless = False
                error_number += 1
                if error_number == 3:
                    errorless = True
                    error_handler.enviarEmail(traceback.extract_stack())
                else:
                    sleep(10)
            if errorless:
                sleep(300)


s = Synchronizer()
s.iniciar_laco()