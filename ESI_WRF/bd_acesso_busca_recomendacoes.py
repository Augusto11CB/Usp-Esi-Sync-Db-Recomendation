import psycopg2
import datetime


class AcessaBD():
    global conn
    global cur

    def __init__(self):
        self.conn = psycopg2.connect("dbname=esifr user=postgres password=erudia host=localhost")
        self.cur = self.conn.cursor()

    def devolveBuscasRecentesCliente(self, idCliente, N):
        self.cur.execute("select busca from buscas where idCliente = " + str(idCliente)
                         + " order by dt desc limit " + str(N) + ";")
        return self.cur.fetchall()

    def devolveBuscasRecentesSemLogin(self, N):
        self.cur.execute("select busca from buscas order by dt desc limit " + str(N) + ";")
        return self.cur.fetchall()

    def devolveNrecomendadosSemLogin(self, N):
        self.cur.execute('select idproduto from visualizacao where dt::date >(CURRENT_DATE - INTERVAL \'3\' day) group by idProduto order by count(*) desc limit \''+str(N)+'\';')
        resp = self.cur.fetchall()
        resposta = [i[0] for i in resp]
        if len(resposta) == N:
            return resposta

        self.cur.execute(
            'select idproduto from visualizacao group by idProduto order by count(*) desc limit \'' + str(
                N) + '\';')
        resp = self.cur.fetchall()
        return [i[0] for i in resp]

    def devolveProdutos(self):
        self.cur.execute("select idProduto, arrayTAG from produto order by vizualizado desc;")
        resp = self.cur.fetchall()
        return [i[0] for i in resp], [i[1] for i in resp], [i[2] for i in resp], [i[3] for i in resp]

    def busque_produtos_categoria_de(self, id_produto):
        self.cur.execute(
            "select categoria from produto where idProduto= \'" + str(id_produto) + "\';")
        resp = self.cur.fetchall()
        try:
            # print(self._arrays_por_id(id_produto))
            a, b = self._devolveProdutosPorCategoria([f[0] for f in resp][0], id_produto)
            return a, b, self._arrays_por_id(id_produto)
        except IndexError:
            return None


    def _arrays_por_id(self, id_produto):
        self.cur.execute(
            "select arrayTAG from tag where idProduto= \'" + str(id_produto) + "\';")
        resp = self.cur.fetchall()
        return [i[0] for i in resp]

    def _devolveProdutosPorCategoria(self, categoria, id_produto):
        self.cur.execute(
            'select m.idProduto, t.arrayTAG from ((select idProduto from produto where categoria = \''+categoria+'\') m left join (select idProduto, arrayTAG from tag) t on m.idProduto = t.idProduto) where m.idProduto !=\''+str(id_produto)+'\';')
        resp = self.cur.fetchall()
        return [i[0] for i in resp], [i[1] for i in resp]#, [i[2] for i in resp], [i[3] for i in resp]


    def _define_ordenacao(self, ordenacao):
        if ordenacao == 'preco':
            return 'order by produto.preco'
        return ''

    # Buscas
    def devolve_produtos_ordenado(self, ordenacao, max_preco, min_preco):
        self.cur.execute('select t.idproduto, t.arrayTAG, produto.preco from produto join tag as t on produto.idProduto = t.idproduto '+self._define_ordenacao(ordenacao)+' and produto.preco between \''+str(min_preco)+'\' and \''+str(max_preco)+'\';')
        resp = self.cur.fetchall()
        return [i[0] for i in resp], [i[1] for i in resp],[i[2] for i in resp]

    def devolve_produtos_categoria(self, categoria, max_preco, min_preco):
        self.cur.execute('select idproduto from produto where categoria = \''+categoria+'\' and preco between \''+str(min_preco)+'\' and \''+str(max_preco)+'\';')
        resp = self.cur.fetchall()
        return [i[0] for i in resp]


    def devolve_produtos_categoria_busca(self, categoria, max_preco, min_preco):
        self.cur.execute('select t.idproduto, t.arrayTAG, produto.preco from produto join tag as t on produto.idProduto = t.idproduto and produto.categoria = \''+categoria+'\' and produto.preco between \''+str(min_preco)+'\' and \''+str(max_preco)+'\';')
        resp = self.cur.fetchall()
        return [i[0] for i in resp], [i[1] for i in resp], [i[2] for i in resp]

    def devolveProdutoComIntervaloDePreco(self, min_preco, max_preco):
        self.cur.execute("select idProduto, arrayTAG, vizualizado, preco from produto where preco between "
                         + str(min_preco) + " and " + str(max_preco) + " order by vizualizado desc;")
        resp = self.cur.fetchall()
        return [i[0] for i in resp], [i[1] for i in resp], [i[2] for i in resp], [i[3] for i in resp]


    def devolveProdutosPorCategoriaComMinPreco(self, min_preco, categoria):
        self.cur.execute("select idProduto, arrayTAG, vizualizado, preco from produto where categoria = \'" + categoria + "\' and "
                         + "preco >= "+ str(min_preco) + " order by vizualizado desc;")
        resp = self.cur.fetchall()
        return [i[0] for i in resp], [i[1] for i in resp], [i[2] for i in resp], [i[3] for i in resp]


    def devolveProdutosPorCategoriaComMaxPreco(self, max_preco, categoria):
        self.cur.execute("select idProduto, arrayTAG, vizualizado, preco from produto where categoria = \'" + categoria + "\' and "
                         + "preco <= "+ str(max_preco) + " order by vizualizado desc;")
        resp = self.cur.fetchall()
        return [i[0] for i in resp], [i[1] for i in resp], [i[2] for i in resp], [i[3] for i in resp]


    def devolveProdutoComIntervaloDePrecoECategoria(self, min_preco, max_preco, categoria):
        self.cur.execute("select idProduto, arrayTAG, vizualizado, preco from produto where categoria = \'" + categoria + "\' and "
                         + "preco between " + str(min_preco) + " and " + str(max_preco) + " order by vizualizado desc;")
        resp = self.cur.fetchall()
        return [i[0] for i in resp], [i[1] for i in resp], [i[2] for i in resp], [i[3] for i in resp]


    # Recomendacoes
    def devolveNrecomendadosParaCliente(self, id_cliente, n):
        self.cur.execute(
            'select DISTINCT visualizacao.idproduto from visualizacao join (select visualizacao.idcliente as cid from '+
            '(select idproduto as ed from visualizacao where idcliente = \''+str(id_cliente)+'\') as produtos_vistos '+
            'join visualizacao on ed = visualizacao.idProduto) as clientes_relacionados on clientes_relacionados.cid = visualizacao.idCliente '+
            'where visualizacao.idProduto not in (select idproduto from visualizacao where idcliente =\''+str(1000)+'\') limit \''+str(n)+'\';')

            #
            #
            # "select DISTINCT idproduto from (select DISTINCT v.idcliente from " +
            # "(select idProduto from visualizacao where idcliente = "+str(id_cliente)+") as t1 " +
            # "join visualizacao v on t1.idproduto = v.idproduto where v.idcliente !="+str(id_cliente)+") as innertab "+
            # "join visualizacao v on innertab.idcliente = v.idcliente and idproduto not in "+
            # "(select idproduto from visualizacao where idcliente ="+str(id_cliente)+") limit "+str(n)+";")
        return [f[0] for f in self.cur.fetchall()]