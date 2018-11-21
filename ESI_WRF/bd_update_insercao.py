import psycopg2
import datetime


class Acesso_bd_updates_insercoes():
    global conn
    global cur

    def __init__(self):
        self.conn = psycopg2.connect("dbname=esifr user=postgres password=erudia host=localhost")
        self.cur = self.conn.cursor()

    def inserirVisualizacao(self, idProduto, idCliente):
        query = 'begin;\nUPDATE produto SET vizualizado = vizualizado + 1 WHERE idProduto = '+str(idProduto)+';\n'
        query+='insert into visualizacao (idProduto, idCliente, dt) VALUES(\''+str(idProduto)+'\',\''+str(idCliente)+'\', current_timestamp);\ncommit;'
        # print(query)
        self.cur.execute(query)
        self.conn.commit()

    def inserirBusca(self, idCliente, busca):
        self.cur.execute("insert into buscas (idCliente, busca, dt) values (%s, %s, %s)",
                         (idCliente, busca, datetime.datetime.now()))
        self.conn.commit()

    def run_query_inserts_updates_deletes(self, query):
        try:
            self.cur.execute(query)
            self.conn.commit()
        except psycopg2.Error as e:
            return e
        return None



class Acesso_bd_updates_insercoes_queries():

    def delete_produto(self, idProduto):
        query = 'delete from produto where idproduto = '+str(idProduto)+';\n'
        return query

    def inserirProduto(self, idProduto, nome, categoria, preco, arraysTAG, textos):
        query = 'insert into produto (idProduto, nome, categoria, preco) VALUES '
        query += '(\''+str(idProduto)+'\',\''+nome+'\',\''+categoria+'\',\''+str(preco)+'\');\n'
        query += 'insert into tag (idProduto, tag_texto, arrayTAG) VALUES'
        for t, a in zip(textos, arraysTAG):
            query += '(\'' + str(idProduto) + '\',\'' + t + '\','
            vetor_guardar = '\'{' + ','.join(str(d) for d in a) + '}\''
            query += vetor_guardar + '),'
            # if(t == arraysTAG[-1]):
            #     query +=';'
            # else:
            #     query += ','
        query = list(query)
        query[-1] = ';'
        query = ''.join(query)
        query += '\n'

        return query


    # def atualizacaoCurtidas(self, idProduto, qtd_curtidas):
    #     query = 'update produto set qtde_curtidas = '+str(qtd_curtidas)+' where idProduto = ' + str(idProduto) + ';\n'
    #     return query

    def atualizeProdutoPreco(self, idProduto, preco):
        query = "update produto set preco = " + str(preco) + " where idProduto =" + str(idProduto) + ";\n"
        return query

    def atualizeProdutoNome(self, idProduto, nome):
        query = "update produto set nome = \'" + nome + "\' where idProduto =" + str(idProduto) + ";\n"
        return query


    def atualizeProdutoTags(self, idProduto, textos, arraysTAG):
        # print(idProduto)
        # print(textos)
        # print(arraysTAG)
        query ='delete from tag where idProduto ='+str(idProduto)+';\n'
        query +='insert into tag (idProduto, tag_texto, arrayTAG) VALUES'
        for t, a in zip(textos, arraysTAG):
            query+='(\''+str(idProduto)+'\',\''+t+'\','
            vetor_guardar = '\'{'+','.join(str(d) for d in a)+'}\''
            query +=vetor_guardar+'),'
            # if(t == arraysTAG[-1]):
            #     query +=';'
            # else:
            #     query += ','
        query = list(query)
        query[-1] = ';'
        query = ''.join(query)
        query+='\n'

        return query


    def atualizeProdutoCategoria(self, idProduto, categoria):
        query = "update produto set categoria = \'" + categoria + "\' where idProduto =" + str(idProduto) + ";\n"
        return query
