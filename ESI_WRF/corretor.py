import re
from collections import Counter
import time
import unicodedata

class Corretor():
    global WORDS
    def __init__(self):
        def words(text): return re.findall(r'\w+', text.lower())
        self.WORDS = Counter(words(open('/home/maxtelll/Desktop/bigpt.txt', encoding='utf-8').read()))

    def P(self, word):
        N = sum(self.WORDS.values())
        "Probability of `word`."
        return self.WORDS[word] / N

    def _correction(self, word):
        "Most probable spelling _correction for word."
        return max(self._candidates(word), key=self.P)

    def _candidates(self, word):
        "Generate possible spelling _corrections for word."
        return (self._known([word]) or self._known(self._edits1(word)) or self._known(self._edits2(word)) or [word])

    def _known(self, words):
        "The subset of `words` that appear in the dictionary of WORDS."
        return set(w for w in words if w in self.WORDS)

    def _edits1(self, word):
        "All edits that are one edit away from `word`."
        letters    = u'aáãâbcçdeẽéêfghiíjklmnoóõpqrstuúvwxyz'
        splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
        deletes    = [L + R[1:]               for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
        replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
        inserts    = [L + c + R               for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)

    def _edits2(self, word):
        "All edits that are two edits away from `word`."
        return (e2 for e1 in self._edits1(word) for e2 in self._edits1(e1))



    def corrige(self, words):
        return [self._correction(word) for word in words]

# busca = ['univerdidade', 'camere', 'blosa', 'unua', 'mochuls', 'valça', 'celulsr','apole', 'escrotor',
#          'univerdidade', 'camere', 'blosa', 'unua', 'mochuls', 'valça', 'celulsr', 'apole', 'escrotor',
#          'univerdidade', 'camere', 'blosa', 'unua', 'mochuls', 'valça', 'celulsr', 'apole', 'escrotor',
#          'univerdidade', 'camere', 'blosa', 'unua', 'mochuls', 'valça', 'celulsr', 'apole', 'escrotor']


# cor = Corretor()
# initial_time = time.time()

# print(cor.corrige('camosa virde rigata'))

# # for d in busca:
# #     a = (cor._correction(d))
# #     print(a)
# # print(cor._correction('enriqueçg'))
# final_time = time.time()

# print('total: ' + str(final_time - initial_time) + " secs")

# # d = open('/home/maxtelll/Desktop/teste.txt', encoding="utf-8").read()
# # d.encode('utf-8').decode('latin-1')
# # print(d)