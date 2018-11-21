from Singleton import Singleton
from representacao import Representacao
from modulo_busca import Pesquisa
import nltk
from string import punctuation
from bd_acesso_busca_recomendacoes import AcessaBD
from bd_update_insercao import Acesso_bd_updates_insercoes
from bd_update_insercao import Acesso_bd_updates_insercoes_queries
from corretor import Corretor
import re
from Busca import Busca


class Interface:
    global stopwords
    global representacao
    global corretor
    global pesquisa

    def __init__(self):
        self.stopwords = nltk.corpus.stopwords.words('portuguese')
        self.representacao = Representacao.instance()
        self.corretor = Corretor()
        self.pesquisa = Pesquisa()

    def _my_tokenizer(self, s):
        resp = ' |\n|!|"|#|$|%|&|\'|\(|\)|\*|\+|\,|\-|\.|/|:|;|<|=|>|\?|@|[|\|]|^|_|`|{|||}|~'
        words = []
        pont = list(punctuation)
        for w in re.split(resp, s):
            if w not in pont and w.lower() not in self.stopwords and len(w) > 0:
                words.append(w.lower())
        return words

    # def nova_busca (self):
    #     return Busca()


    def _representacao(self, busca):
        words = self._my_tokenizer(busca)
        words = self.corretor.corrige(words)
        return self.representacao.devolveVetor(words)

    def _ordene(self, ids, lista):
        return (list(t) for t in zip(*sorted(zip(lista, ids))))


    # produto

    def realiza_operacoes_atualizacao_bd(self, insert_dict, update_dict, delete_list):
        ac = Acesso_bd_updates_insercoes_queries()
        r = self.representacao
        queryDeAtualizacao = 'begin;\n'

        for insercao in insert_dict:
            queryDeAtualizacao += ac.inserirProduto(insercao["id_produto"], insercao["nome"],
                            insercao["categoria_log"],insercao["preco"],[r.devolveVetor(self.corretor.corrige(t)) for t in insercao["tags_log"]] ,insercao["tags_log"])
        for atualizacao in update_dict:
            if atualizacao["nome"]:
                queryDeAtualizacao += ac.atualizeProdutoNome(atualizacao["id_produto"], atualizacao["nome"])
            if atualizacao["categoria_log"]:
                queryDeAtualizacao += ac.atualizeProdutoCategoria(atualizacao["id_produto"], atualizacao["categoria_log"])
            if atualizacao["preco"]:
                queryDeAtualizacao += ac.atualizeProdutoPreco(atualizacao["id_produto"], atualizacao["preco"])

            if atualizacao["tags_log"]:
                queryDeAtualizacao += ac.atualizeProdutoTags(atualizacao["id_produto"], atualizacao["tags_log"],
                                                             [r.devolveVetor(self.corretor.corrige(t)) for t in atualizacao["tags_log"]])

        for id_p in delete_list:
            queryDeAtualizacao += ac.delete_produto(id_p)

        queryDeAtualizacao += 'commit;\n'

        print(queryDeAtualizacao)
        return Acesso_bd_updates_insercoes().run_query_inserts_updates_deletes(queryDeAtualizacao)



    # def delete_produto(self, idProduto):
    #     Acesso_bd_updates_insercoes.delete_produto(idProduto)
    #
    # def insere_novo_produto(self, idProduto, nome, categoria, preco, arraysTAG, textos):
    #     Acesso_bd_updates_insercoes.inserirProduto(idProduto, nome, categoria, preco, arraysTAG, textos)

    # def atualizacaoCurtidas(self, idProduto, qtd_curtidas):
    #     Acesso_bd_updates_insercoes.atualizacaoCurtidas(idProduto, qtd_curtidas)
    #
    # def atualizeProdutoPreco(self, idProduto, preco):
    #     Acesso_bd_updates_insercoes.atualizeProdutoPreco(idProduto, preco)
    #
    # def atualizeProdutoNome(self, idProduto, nome):
    #     Acesso_bd_updates_insercoes.atualizeProdutoNome(idProduto, nome)
    #
    # def atualizeTags(self, idProduto, textos, arraysTAG):
    #     Acesso_bd_updates_insercoes.atualizeProdutoTags(idProduto, textos, arraysTAG)
    #
    # def atualizeCategorias(self, idProduto, categoria):
    #     Acesso_bd_updates_insercoes.atualizeProdutoCategoria(idProduto, categoria)

    #busca
    def busque_n_relacionados(self, id_cliente, id_produto, n=5):
        if id_cliente:
            self._add_visualizacao(id_produto, id_cliente)
        ids, vetores, valores_produto = AcessaBD().busque_produtos_categoria_de(id_produto)

        return self.pesquisa.busca_n_relacionados(valores_produto, vetores, ids, n)


    def busque(self, busca):
        if busca.id_cliente and busca.busca:
            Acesso_bd_updates_insercoes().inserirBusca(busca.id_cliente, busca.busca)
        return self._devolveProdutos(busca.busca, busca.min_price, busca.max_price, busca.categoria, busca.ordenacao)

    def _add_visualizacao(self, idProduto, idCliente):
        Acesso_bd_updates_insercoes().inserirVisualizacao(idProduto=idProduto, idCliente=idCliente)

    def _inserir_busca(self, idCliente, busca):
        Acesso_bd_updates_insercoes().inserirBusca(idCliente, busca)

    def _define_ordenacao(self, ordenacao, list, ):
        if ordenacao == 'preco':
            return 'order by produto.preco'


    def _devolveProdutos(self, busca, min_preco, max_preco, categoria, ordenacao):
        # if categoria and max_preco and min_preco and busca:
        #     ids, base, vizualizacao, preco = AcessaBD().devolveProdutoComIntervaloDePrecoECategoria(min_preco,
        #                                                                                              max_preco,
        #                                                                                              categoria)
        #     return self._ordene(self.pesquisa.busca_limite_distancia(self._representacao(busca), base, ids),
        #                         self._define_ordenacao(ordenacao, vizualizacao, preco))
        #
        # if categoria and max_preco and busca:
        #     ids, base, vizualizacao, preco = AcessaBD().devolveProdutosPorCategoriaComMaxPreco(max_preco, categoria)
        #     return self._ordene(self.pesquisa.busca_limite_distancia(self._representacao(busca), base, ids),
        #                         self._define_ordenacao(ordenacao, vizualizacao, preco))
        #
        # if categoria and min_preco and busca:
        #     ids, base, vizualizacao, preco = AcessaBD().devolveProdutosPorCategoriaComMinPreco(min_preco, categoria)
        #     return self._ordene(self.pesquisa.busca_limite_distancia(self._representacao(busca), base, ids),
        #                         self._define_ordenacao(ordenacao, vizualizacao, preco))
        #
        # if min_preco and max_preco and busca:
        #     ids, base, vizualizacao, preco = AcessaBD().devolveProdutoComIntervaloDePreco(min_preco, max_preco)
        #     return self._ordene(self.pesquisa.busca_limite_distancia(self._representacao(busca), base, ids),
        #                         self._define_ordenacao(ordenacao, vizualizacao, preco))

        if categoria and busca:
            ids, base, preco = AcessaBD().devolve_produtos_categoria_busca(categoria, max_preco, min_preco)
            print(base)
            if len(base) == 0:
                return None
            return self.pesquisa.busca_limite_distancia(self._representacao(busca), base, ids)

        if categoria:
            ids = AcessaBD().devolve_produtos_categoria(categoria, max_preco, min_preco)
            return ids

        if busca:
            ids, base, preco = AcessaBD().devolve_produtos_ordenado(ordenacao, max_preco, min_preco)
            if len(base) == 0:
                return None
            return self.pesquisa.busca_limite_distancia(self._representacao(busca), base, ids)

        ids, base, vizualizacao, preco = AcessaBD().devolveProdutos()
        return ids



    # recomendacoes

    def devolveNprodutosRecomendados(self, id_cliente, N):
        return AcessaBD().devolveNrecomendadosParaCliente(id_cliente, N)

    def devolveRecomendacaoPaginaInicial(self, N):
        return AcessaBD().devolveNrecomendadosSemLogin(N)

