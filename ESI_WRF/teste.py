from gensim.models import KeyedVectors
from sklearn.neighbors import NearestNeighbors
import psycopg2
from decimal import Decimal
import numpy as np
import random
from corretor import Corretor

print(Corretor().corrige(words=["inaninação"]))


# X = [[0,0], [1,1], [5,5], [-2,-2], [10,10]]
# Y = [[Decimal(0),Decimal(0)],[Decimal(6),Decimal(6)]]

import sys

# sys.path.append('/home/maxtelll/PycharmProjects/ic/facets')
#
#
# conn = psycopg2.connect("dbname=esifr user=postgres password=Alphabet@6494 host=localhost")
# cur = conn.cursor()
#
# cur.execute('select idproduto from produto where idproduto in %s order by preco;', ( tuple([1,5,2,3]),))
# resp = cur.fetchall()
# ids = [i[0] for i in resp]
# print(ids)
# print(nome)
# print(np.array(tag))
a = [1,1]
# m = KeyedVectors.load_word2vec_format('/home/maxtelll/Documents/USP/sextoSemestre/esi/projeto/cbow_s50.txt',
#                                           unicode_errors="ignore")
# model = m.wv
# model.init_sims(replace=True)
# d = open('/home/maxtelll/Documents/USP/sextoSemestre/esi/projeto/s.txt','w+')
# g = [f for f in model.vocab]
#
# saida = ''
# for h in g:
#     saida+=h+'\n'
#
# d.write(saida)
# d.close()

# print(a[100])


# print(X)
# nn = NearestNeighbors(2, metric='euclidean', algorithm='brute').fit(X)
# d,i = nn.kneighbors(Y)
# print(d)
# print(i)

# a = [1,1]
# print(a[100])


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
insercoes = []
i1 = {
    "categoria_log": "camiseta",
    "id_log": 8,
    "id_produto":3005,
    "nome": "camiseta branca regata",
    "preco": 19.95,
    "tags_log": [
      "camisetu","estilosu"
    ],
    "type_log": "INSERT"
  }
insercoes.append(i1)
# i2 = {
#     "categoria_log": "calça",
#     "id_log": 8,
#     "id_produto":3001,
#     "nome": "calça jeans",
#     "preco": 120.00,
#     "tags_log": [
#       "calça","moda", "feminina","nova"
#     ],
#     "type_log": "INSERT"
#   }
# insercoes.append(i2)
# #
# i3 = {
#     "categoria_log": "calça",
#     "id_log": 8,
#     "id_produto":3002,
#     "nome": "calça social",
#     "preco": 99.95,
#     "tags_log": [
#       "calça social","escritório", "masculina","preta"
#     ],
#     "type_log": "INSERT"
#   }
# insercoes.append(i3)
#
atualizacoes = []
#  120 | 16 | tênis | calçado | 62.69,azul,mola,calçado,nova

a1 = {
    "categoria_log": "",
    "id_log": 8,
    "id_produto":120,
    "nome": "",
    "preco": '',
    "tags_log": [
      "corroda","confortivel", "origimal"
    ],
    "type_log": "UPDATE"
  }
atualizacoes.append(a1)
  # 632 | 14 | sapato masculino | calçado | 74.89, viagem, moderno, verão
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
#
# # 200 | 18 | calça feminina | calça | 63.99 , moderno, empresa, trabalho
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
#
delete_list = ['20','30','62']
# print("carregou")
a = Interface()
sugestoes = ['sapat', 'calça', 'camiseta', 'couro','blusa', 'jeans','caqui','vermelha','carteira','camiseta','bolsa']
inicial = time.time()

print(a.retorne_sugestoes('cou'))

# for _ in range(1000):
#     print(a.retorne_sugestoes(random.choice(sugestoes)))

# t = a.realiza_operacoes_atualizacao_bd(insercoes, atualizacoes, delete_list)
# print(t)

# print(time.time()-inicial)
# b = Busca()
# b.atribui_ordenacao('preco')
# b.atribui_busca('estilo bermuds vdauvdsau verão')
# b.atribui_categoria('bermuda')
# b.atribui_id(10)
# b.atribui_valor_maximo(90)
# b.atribui_valor_minimo(79)

# print(a.busque(b))
# print('foi')
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


from random import randint
import random

# qtd, ids = a.retorne_buscas_n_dias(2)
# print(qtd)
# print(ids)

# print(a[100])

# print('inicio')
import threading


# def faz(a):
    # a = Interface()
    # b = Busca()
    # b.atribui_ordenacao('preco')
#     b.atribui_busca('estilo bermuds vdauvdsau verão')
#     # b.atribui_categoria('bermuda')
#     b.atribui_id(randint(100, 500))
#     if random.random() > 0.6:
#         b.atribui_valor_maximo(90)
#     elif random.random() > 0.6:
#         b.atribui_valor_minimo(79)
#     else:
#         b.atribui_valor_maximo(100)
#         b.atribui_valor_minimo(20)
# # print(id(b))
#     a.busque(b)

# t = threading.Thread(target=faz,args=(a,))
# t.start()
# ti = time.time()
# for _ in range(100):
# #
# sugestoes = ['sapat', 'calça', 'camiseta', 'couro','blusa', 'jeans','caqui','vermelha','carteira','camiseta','bolsa']
categoria = {
'roupa social':'camisa,gravata,sapato,gravata,camisa social,listrada,escritório,social,branco,preto,negócios,chefe,branca',
'bolsa':'bolsa vermelha,bolsa da moda,bolsa de couro,mulher,fashion,prático,moda,facilidade,festa,couro',
'mochila':'mochila escolar,mochila de viagem,estudante,viagem,praticidade,bagagem,couro,impermeável,grande carga,preta',
'acessórios':'óculos,carteira de couro,relógio,colar,corrente,óculos de sol,moda,couro,importado,escritório,jóias',
'blusa':'blusa de lã,jaqueta,jaqueta de couro,couro,inverno,aquecimento,preta,branca,cinza,azul,rosa,bege',
'camiseta':'camiseta branca,camiseta regata,bandas,informal,regata,esporte,academia,futebol,preta,branca,cinza,azul,vermelho,amarelo',
'calça':'calça jeans,calça social,calça caqui,longa,jeans,confortável,preta,branca,cinza,azul,moletom',
'calçado':'tênis,tênis corrida,tênis com amortecedor,mola,amortecedor,confortável,preta,branca,cinza,azul,esporte,corrida,academia,exercício,camisa preta chefe'
}

# branco
#  chefe
#  negócios
#  branca
#  listrada
#  roupa social
#  florido



# print(a.busque_n_relacionados(id_produto=1235))
# print('recomendacoes')
# print(a.devolveNprodutosRecomendados(5, 10))
# print(a.devolveNprodutosRecomendados(20, 10))
# print(a.devolveNprodutosRecomendados(80, 2))
# print(a.devolveNprodutosRecomendados(1000, 10))
# print(a.devolveRecomendacaoPaginaInicial(10))

# b = Busca()
# # b.atribui_ordenacao('preco')
# # cat = random.choice(list(categoria.keys()))
# # digitado = random.choice(categoria[cat].split(','))
# # print(digitado)
# b.atribui_busca('camisa preta chefe')
# b.atribui_categoria('roupa social')
# b.atribui_valor_maximo(40)
# b.atribui_ordenacao('popularidade')
# # [1269, 819, 204, 1518, 2448, 938, 1753, 2909, 734]
# print(a.busque(b))
# a=[1]
# print(a[10])


b = Busca()
b.atribui_categoria('blusa')
b.atribui_busca('blusa preta')
b.atribui_ordenacao('maior_preco')
# else:
#     b.atribui_valor_maximo(100)
    # b.atribui_valor_minimo(5)
# # print(id(b))

# print(a.busque(b))


inicial = time.time()
# for _ in range(100):
#     b = Busca()
#     # b.atribui_ordenacao('preco')
#     cat = random.choice(list(categoria.keys()))
#     digitado = random.choice(categoria[cat].split(','))
#     # print(digitado)
#     b.atribui_busca(digitado)
#     if random.random() > 0.7:
#         b.atribui_categoria(cat)
#     if random.random() > 0.6:
#         b.atribui_ordenacao(random.choice(['menor_preco', 'maior_preco','popularidade']))
#     if random.random() > 0.2:
#         b.atribui_id(randint(0, 500))
#     if random.random() > 0.6:
#         b.atribui_valor_maximo(90)
#     elif random.random() > 0.6:
#         b.atribui_valor_minimo(10)
#     # else:
#     #     b.atribui_valor_maximo(100)
#         # b.atribui_valor_minimo(5)
#     # # print(id(b))
#
#     print(len(a.busque(b)))

# print(time.time()-inicial)
# print('foi esse')


# print(time.time()-ti)
# foda-se
# print('comeca busca')
# initial_time = time.time()
#
# print('recomendacoes')
# print(a.devolveNprodutosRecomendados(5, 10))
# print(a.devolveNprodutosRecomendados(20, 10))
# print(a.devolveNprodutosRecomendados(800000, 10))
# print(a.devolveRecomendacaoPaginaInicial(10))

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
