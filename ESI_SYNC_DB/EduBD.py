import requests

class EduBD:
    WEBSITE = 'https://dry-escarpment-83331.herokuapp.com/'

    def get_current_version(self, id_log):
        r = requests.get(self.WEBSITE + 'log/last_id=' + str(id_log) )
        return r.text

    def get_produto(self, id_prod):
        r = requests.get(self.WEBSITE + 'produto/' + str(id_prod))
        return r.text

    def __init__(self):
        pass
