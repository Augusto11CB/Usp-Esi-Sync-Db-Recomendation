from collections import Counter

import numpy as np
from sklearn.neighbors import NearestNeighbors
import math
import time
import sys
from representacao import Representacao
import random, _thread as thread
from sklearn.neighbors import radius_neighbors_graph

class Pesquisa():

    def _nearest_neighbors(self, values, base, nbr_neighbors = 5):
        nn = NearestNeighbors(nbr_neighbors, metric='euclidean', algorithm='brute').fit(base)
        return nn.kneighbors(values)


    def busca_n_relacionados(self, values, base, Y, n=5):
        base = np.array(base)
        values = np.array(values)
        # print(len(values))
        # print(base)
        # print(Y)
        distances, indices = self._nearest_neighbors(values, base, int(len(base)/10))
        # print(indices)

        m = indices.flatten(1).tolist()
        # m.append(4)
        # m.append(16)
        # print(m)
        cnt = Counter(m)
        A = [f[0] for f in cnt.most_common(n)]
        return [Y[a] for a in A]


    def busca_limite_distancia(self, values, base, ids):
        base = np.array(base)
        values = np.array([values])
        # s = 0
        # for i in range(len(base)):
        #     for a in base[i]:
        #         s+=1
        #         if a != a or a > 1 or a < -1:
        #             print(ids[i])
        #             print(a)
        #             print(s)
        # print(len(base))
        # print(values)

        distances, indices = self._nearest_neighbors(values, base, int(len(ids)/10))

        # print(distances)
        # print(type(indices[0]))
        # print(len(list(set(indices[0]))))

        resposta = [ids[indices[0][l]] for l in range(len(indices[0])) if distances[0][l] < 1]
        # print(resposta)
        return list(set(resposta))
        # base.insert(0, values)
        # nn = radius_neighbors_graph(base, 10.0, mode='connectivity',
        #                            metric='manhattan', include_self=True)
        # print(nn.toarray())
        # return [ids[a] for a in range(len(nn.toarray()[0,1:])) if nn.toarray()[0,1:][a]]


# tags = ['camiseta branca', 'computador i7', 'processador i7', 'blusa verão', 'camiseta regata', 'calça',
#         'laptop i7', 'camisa social', 'camiseta social', 'calça jeans', 'computador i7', 'processador i7',
#         'blusa verão', 'camiseta regata', 'calça', 'laptop i7', 'camisa social', 'camiseta social',
#         'calça jeans', 'computador i7', 'processador i7', 'blusa verão', 'camiseta regata', 'calça',
#         'laptop i7', 'camisa social', 'camiseta social', 'calça jeans', 'computador i7', 'processador i7',
#         'blusa verão', 'camiseta regata', 'calça', 'laptop i7', 'camisa social', 'camiseta social',
#         'calça jeans', 'computador i7', 'processador i7', 'blusa verão', 'camiseta regata', 'calça',
#         'laptop i7', 'camisa social', 'camiseta social', 'calça jeans', 'computador i7', 'processador i7',
#         'blusa verão', 'camiseta regata', 'calça', 'laptop i7', 'camisa social', 'camiseta social',
#         'calça jeans', 'computador i7', 'processador i7', 'blusa verão', 'camiseta regata', 'calça',
#         'laptop i7', 'camisa social', 'camiseta social', 'calça jeans']
#


# X = [[0,0], [1,1], [5,5], [-2,-2], [-5,-6], [50, 50], [3, 200], [-1, 100]]
# Y = [1, 2, 3, 4, 10, 23, 54, 18]
#
# p = Pesquisa()

# print(p.busca_n_relacionados([10,10], X, Y, 3))

# def pegaPesquisa():
#     return tags[random.randint(0, len(tags))]

# vetores = []
# print("comecou a carregar")
# r = Representacao()
# print("carregou o primeiro")


# def execucao(p, i):
#     print(r.devolveVetor(p))

# initial_time = time.time()
# variasThreads = []
# for i in range(30):
#     variasThreads.append(thread.start_new_thread(execucao,(pegaPesquisa(), i)))
# final_time = time.time()
#
# print('total: ' + str(final_time - initial_time) + " secs")
#
# print(variasThreads)

# for t in tags:
#     vetores.append(r.devolveVetor(t))
#
# print('carregou')
# X = np.array(vetores)
# print(sys.getsizeof(X))
# print(X)

# X = np.array([[-6, -7], [0, -1], [-4, -6], [1, 1], [12, 1], [1, 1]])
# nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)
# p = Pesquisa(X)
# teste = np.array([r.devolveVetor('camisa')])
# teste = np.array([[0, 1]])
# distances, indices = nbrs.kneighbors(teste)

# initial_time = time.time()
# dists, idxs = p.nearest_neighbors(teste)
# final_time = time.time()

# print('total: ' + str(final_time - initial_time) + " secs")

# for f in idxs[0]:
    # print(f)

# print(dists)
#
# for w in model.wv.most_similar_cosmul('parede'):
#     print(w)