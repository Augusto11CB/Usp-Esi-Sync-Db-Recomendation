from gensim.models import KeyedVectors
import gensim
import numpy as np

from Singleton import Singleton

@Singleton
class Representacao:
    global model
    def __init__(self):
        self.model = KeyedVectors.load_word2vec_format('resourcesToSearch/cbow_s50.txt',
                                          unicode_errors="ignore")
        self.model = self.model.wv
        self.model.init_sims(replace=True)

    def devolveVetor(self, pesquisa):
        mean = []
        # for palavra in pesquisa:
        #     mean.append(self.model[palavra])

        for word in pesquisa:
            if isinstance(word, np.ndarray):
                mean.append(word)
            elif word in self.model.vocab:
                mean.append(self.model.syn0norm[self.model.vocab[word].index])

            if not mean:
                return np.zeros(50)

        return gensim.matutils.unitvec(np.array(mean).mean(axis=0)).astype(np.float32)



