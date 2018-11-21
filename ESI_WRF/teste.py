from sklearn.neighbors import NearestNeighbors
X = [[0,0], [1,1], [5,5], [-2,-2], [10,10]]
Y = [[-1,-1],[6,6]]
# print(X)
# nn = NearestNeighbors(2, metric='euclidean', algorithm='brute').fit(X)
# d,i = nn.kneighbors(Y)
# print(d)
# print(i)


# from sklearn.neighbors import radius_neighbors_graph
# A = radius_neighbors_graph(X, 15.5, mode='connectivity',
#                            include_self=True)

# print(A.toarray())
# a = A.toarray()[0,1:]
# print([Y[a] for a in range(len(A.toarray()[0,1:])) if A.toarray()[0,1:][a]])
# if a:
# print(a[0])
# from bd_acesso import AcessaBD
# from representacao import Representacao
# from corretor import Corretor
# import random
#
# tags = ['camiseta branca', 'blusa inverno', 'camiseta regata', 'calça jeans', 'camisa social', 'camisa social branca',
#         'calça jeans', 'calça social', 'blusa verão', 'camiseta regata', 'calça', 'camisa social azul', 'camiseta branca lisa',
#         'calça jeans', 'computador i7', 'processador i7', 'camiseta regata listrada', 'calça cáqui',
#         'camisa social manga longa', 'camiseta social', 'calça jeans', 'notebook i7', 'processador i7',
#         'blusa verão', 'camiseta regata', 'calça preta', 'laptop i7', 'camisa social', 'camisa social',
#         'camiseta social', 'calça jeans']
#
# cat = ['camisa', 'calça', 'sapato', 'eletrônico', 'blusa']
# def random_floats(low, high, size):
#     return [random.uniform(low, high) for _ in range(size)]
#
# Y = [i for i in range(len(tags))]
# preco = random_floats(15, 50, len(Y))
#
# categorias = [random.choice(cat) for _ in range(len(Y))]
# bd = AcessaBD()
# r = Representacao()
# c = Corretor()
# print(categorias)
# print(Y)
# print(preco)

# from string import punctuation
# import re
# import nltk
#
# stopwords = nltk.corpus.stopwords.words('portuguese')
# def _my_tokenizer(s):
#     resp = ' |\n|!|"|#|$|%|&|\'|\(|\)|\*|\+|\,|\-|\.|/|:|;|<|=|>|\?|@|[|\|]|^|_|`|{|||}|~'
#     words = []
#     pont = list(punctuation)
#     for w in re.split(resp, s):
#         if w not in pont and w.lower() not in stopwords and len(w) > 0:
#             words.append(w.lower())
#     return words
#
#
# for i in range(len(Y)):
#     words = _my_tokenizer(tags[i])
#     words = c.corrige(words)
#     values = r.devolveVetor(words)
#     values = values.tolist()
#     bd.inserirProduto(Y[i], categorias[i], values, preco[i])

import time

from Busca import Busca
# from bd_update_insercao import Acesso_bd_updates_insercoes
# bd = Acesso_bd_updates_insercoes();
# idP = 5000
# textos = ['carne', 'arroz', 'feijão', 'batata']
# arrayTags = [[0, 1, 0.2, 5],
#              [0, 1, 0, 6],
#              [0, 1, 2, 7],
#              [1, 1, 1, 12]]
# a, b = bd.run_query_inserts_updates_deletes('update produto set pregco = 99.99 where idProduto = 10;')
# print(type(b))

from Interface import Interface
from bd_acesso_busca_recomendacoes import AcessaBD

# b = AcessaBD()
# for s in b._arrays_por_id(4):
#     print(len(s))

# print(a.busque_n_relacionados(5,40))
# insercoes = []
# i1 = {
#     "categoria_log": "camiseta",
#     "id_log": 8,
#     "id_produto":1008,
#     "nome": "camiseta branca regata",
#     "preco": 99.95,
#     "tags_log": [
#       "camiseta","estilosu", "genuino"
#     ],
#     "type_log": "INSERT"
#   }
# insercoes.append(i1)
# i2 = {
#     "categoria_log": "calça",
#     "id_log": 8,
#     "id_produto":1006,
#     "nome": "calça jeans",
#     "preco": 120.00,
#     "tags_log": [
#       "calça","moda", "feminina","nova"
#     ],
#     "type_log": "INSERT"
#   }
# insercoes.append(i2)
#
# i3 = {
#     "categoria_log": "calça",
#     "id_log": 8,
#     "id_produto":1007,
#     "nome": "calça social",
#     "preco": 99.95,
#     "tags_log": [
#       "calça social","escritório", "masculina","preta"
#     ],
#     "type_log": "INSERT"
#   }
# insercoes.append(i3)

atualizacoes = []
#  120 | 16 | carteira de couro preta | acessórios | 21.44, camiseta, verão, escritório
# a1 = {
#     "categoria_log": "acessórios",
#     "id_log": 8,
#     "id_produto":120,
#     "nome": "carteira de couro decorada",
#     "preco": 50.00,
#     "tags_log": [
#       "social","escritório", "masculina","estiloso", "genuino"
#     ],
#     "type_log": "UPDATE"
#   }
# atualizacoes.append(a1)
#   632 | 14 | sapato masculino | calçado | 74.89, viagem, moderno, verão
# a2 = {
#     "categoria_log": "",
#     "id_log": 8,
#     "id_produto":632,
#     "nome": "",
#     "preco": '',
#     "tags_log": [
#       "masculina","camisa", "genuino"
#     ],
#     "type_log": "UPDATE"
#   }
# atualizacoes.append(a2)

# 200 | 18 | calça feminina | calça | 63.99 , moderno, empresa, trabalho
# a3 = {
#     "categoria_log": "calça",
#     "id_log": 8,
#     "id_produto":200,
#     "nome": "",
#     "preco": 35.20,
#     "tags_log": [],
#     "type_log": "UPDATE"
#   }
# atualizacoes.append(a3)

# delete_list = []# ['20','30','62']
# print("carregou")
# t = a.realiza_operacoes_atualizacao_bd(insercoes, atualizacoes, delete_list)
# print(t)

# [
#   {
#     "categoria_log": "string",
#     "id_log": 0,
#     "id_produto": 0,
#     "nome": "string",
#     "preco": 0,
#     "tags_log": [
#       "string"
#     ],
#     "type_log": "INSERT"
#   }
# ]




#
# for f, b in zip(textos, arrayTags):
#     print(f, b)

# bd.atualizeProdutoTags(idProduto=idP, textos=textos, arraysTAG=arrayTags)
# bd.inserirProduto(idProduto=idP, nome='qualquer nome',categoria='essa categoria', preco=20.50, textos=textos, arraysTAG=arrayTags)

# bd.inserirVisualizacao(4,5)
# bd.atualizacaoCurtidas(4,50)
# bd.atualizeProdutoPreco(4, 20.65)
# from Interface import Inter
# bd.atualizeProdutoCategoria(4, 'acessórios')
# bd.atualizeProdutoNome(4, 'óculos de sol armani')
# bd.inserirBusca(1000, 'busca qualquer coisa')
# face



# print('inicio')
a = Interface()


#
b = Busca()
# b.atribui_ordenacao('preco')
b.atribui_busca('estilo bermuda verão')
b.atribui_categoria('bermuda')
b.atribui_id(257)
b.atribui_valor_maximo(90)
# b.atribui_valor_minimo(79)

# print(id(b))
print(a.busque(b))
# print('comeca busca')
# initial_time = time.time()
#
print(a.devolveNprodutosRecomendados(5, 10))
print(a.devolveNprodutosRecomendados(200, 10))
print(a.devolveNprodutosRecomendados(1000, 10))
print(a.devolveRecomendacaoPaginaInicial(10))

# print(len(i.busque(b)))

# print('carregou')
# final_time = time.time()
# print('total: ' + str(final_time - initial_time) + " secs")
# c = Busca.instance()
# b.n = 'sim'
# print(b.n)
# print(c.n)

# i = Interface()

# print(i.devolveProdutos(None, None, None, 'calça'))

# bd.devolveProdutoComIntervaloDePrecoECategoria(1, 100, 'camisa')

# def _ordene(ids, lista):
#     return (list(t) for t in zip(*sorted(zip(lista, ids))))
#
# l1 = [2, 2, 5, 1, 0, 10]
# l2 = ['dois1', 'dois2', 'cinco', 'um', 'zero', 'dez']
# l1, l2 = _ordene(l2, l1)
#
# print(l1)
# print(l2)
