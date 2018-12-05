import psycopg2
import datetime


class AcessaBD_relatorios():
    global conn
    global cur

    def __init__(self):
        self.conn = psycopg2.connect("dbname=esifr user=postgres password=erudia host=localhost")
        self.cur = self.conn.cursor()

    def devolva_mais_pesquisados_n_dias(self, dias):
        if not type(dias) ==int:
            return []
        self.cur.execute('select count(*), busca from buscas where  dt::date >(CURRENT_DATE - INTERVAL \''+str(dias)+'\' day) group by busca order by count(*) desc;')
        resp = self.cur.fetchall()
        return [i[0] for i in resp],[i[1] for i in resp]
