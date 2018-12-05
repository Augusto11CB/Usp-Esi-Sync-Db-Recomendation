import numpy as np
import random


nPessoas = 8000
nPontos = 39

X = np.array([58, 40, 35, 28, 18, 14, 15, 13, 12, 16, 
                 13, 17, 19, 21, 21, 9, 7, 10,20, 21, 
                 22, 25, 21, 4, 3, 4, 6,10, 8, 12, 
                 19, 15, 12, 9, 7, 10, 9, 12])
Y = np.array([X[0]])
passageiros = np.zeros(38)
for i in range(1, nPontos-1):
    aux = np.array([Y[i-1]+X[i]])
    Y = np.append(Y, aux)

# print(Y)
# print(X)


soma = sum(X)
for p in range(nPessoas):
    pos = random.randint(0, soma)
    for v in range(nPontos-1):
        if v == 0:
            if pos <= Y[v] and v ==0:
                passageiros[0] +=1

        elif pos <= Y[v] and pos > Y[v-1]:
            passageiros[v] +=1

print(passageiros)
    # print(pos)
#                            0, 1, 2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23
horariosDePico = np.matrix([[0, 0, 0, 0,15,15,13,10, 6, 2, 2, 1, 1, 2, 1, 2, 1, 1, 2, 5, 0, 0, 0, 0], #0
                            [0, 0, 0, 0,10,14,10, 8, 7, 3, 2, 1, 2, 2, 1, 1, 2, 3, 2, 1, 0, 0, 0, 0], #1
                            [0, 0, 0, 0, 9,14,10, 9, 8, 2, 1, 1, 2, 2, 4, 5, 2, 3, 2, 1, 0, 0, 0, 0], #2
                            [0, 0, 0, 0, 5,12, 8, 5, 8, 2, 1, 1, 2, 1, 2, 3, 2, 3, 2, 1, 0, 0, 0, 0], #3
                            [0, 0, 0, 0, 2,12,11, 5, 8, 2, 1, 1, 2, 2, 4, 5, 2, 3, 2, 1, 0, 0, 0, 0], #4
                            [0, 0, 0, 0, 2, 1, 4, 2, 2, 2, 1, 1, 2, 2, 4, 5, 2, 3, 2, 1, 0, 0, 0, 0], #5
                            [0, 0, 0, 0, 1, 1, 4, 3, 3, 2, 1, 1, 2, 2, 4, 5, 2, 3, 2, 1, 0, 0, 0, 0], #6
                            [0, 0, 0, 0, 1, 1, 3, 3, 1, 2, 1, 1, 2, 2, 4, 5, 2, 3, 2, 1, 0, 0, 0, 0], #7
                            [0, 0, 0, 0, 1, 1, 2, 2, 1, 1, 2, 1, 8, 2, 1, 3, 2, 1, 2, 1, 0, 0, 0, 0], #8
                            [0, 0, 0, 0, 1, 1, 1, 1, 2, 1, 2, 1, 8, 2, 1, 3, 2, 1, 2, 1, 0, 0, 0, 0], #9
                            [0, 0, 0, 0, 0, 1, 2, 1, 3, 1, 1, 1, 1, 2, 1, 3, 2, 1, 2, 1, 0, 0, 0, 0], #10
                            [0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 2,10,12,11, 0, 0, 0, 0], #11
                            [0, 0, 0, 0, 0, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 9, 8,10, 0, 0, 0, 0], #12
                            [0, 0, 0, 0, 0, 1, 1, 1, 3, 1, 1, 2, 1, 2, 1, 1, 2, 9, 9,11, 0, 0, 0, 0], #13
                            [0, 0, 0, 0, 0, 1, 1, 1, 4, 1, 1, 2, 1, 2, 1, 1, 1, 9, 9,12, 0, 0, 0, 0], #14
                            [0, 0, 0, 0, 0, 1, 3, 1, 4, 1, 1, 1, 1, 2, 1, 1, 2, 9, 2, 1, 0, 0, 0, 0], #15
                            [0, 0, 0, 0, 0, 1, 2, 2, 5, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0], #16
                            [0, 0, 0, 0, 0, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 0, 0, 0, 0], #17
                            [0, 0, 0, 0, 0, 1, 1, 2, 1, 1, 3, 1, 1, 2, 1, 1, 1, 5, 2, 1, 0, 0, 0, 0], #18
                            [0, 0, 0, 0, 0, 2, 2, 2,16,15,15, 2, 1, 1, 1, 2, 1, 1, 2, 1, 0, 0, 0, 0], #19
                            [0, 0, 0, 0, 0, 2, 1, 2,13, 5, 5, 6, 8, 2, 1, 1, 1, 2, 2, 1, 0, 0, 0, 0], #20
                            [0, 0, 0, 0, 0, 1, 1, 2, 6,12,13, 1, 8, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], #21
                            [0, 0, 0, 0, 0, 1, 1, 2, 4, 8,13, 2, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], #22
                            [0, 0, 0, 0, 0, 1, 1, 2, 3, 6, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], #23
                            [0, 0, 0, 0, 0, 3, 1, 1, 6, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], #24
                            [0, 0, 0, 0, 0, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 0, 0, 0, 0], #25
                            [0, 0, 0, 0, 0, 1, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 0, 0, 0], #26
                            [0, 0, 0, 0, 0, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 0, 0, 0, 0], #27
                            [0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], #28
                            [0, 0, 0, 0, 0, 0, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 0, 0, 0, 0], #29
                            [0, 0, 0, 0, 0, 0, 1, 2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 5, 1, 0, 0, 0, 0], #30
                            [0, 0, 0, 0, 0, 0, 3, 1, 1, 2, 2, 3, 1, 2, 1, 3, 1, 1, 1, 2, 0, 0, 0, 0], #31
                            [0, 0, 0, 0, 0, 0, 3, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0], #32
                            [0, 0, 0, 0, 0, 0, 3, 1, 2, 1, 3, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0], #33
                            [0, 0, 0, 0, 0, 1, 3, 2, 1, 2, 3, 2, 3, 2, 1, 1, 2, 1, 2, 3, 0, 0, 0, 0], #34
                            [0, 0, 0, 0, 0, 1, 3, 5, 1, 1, 3, 1, 3, 1, 1, 2, 2, 1, 3, 2, 0, 0, 0, 0], #35
                            [0, 0, 0, 0, 0, 1, 3, 6, 2, 2, 3, 2, 8, 2, 1, 3, 2, 5, 5, 2, 0, 0, 0, 0], #36
                            [0, 0, 0, 0, 0, 1, 3, 7, 6, 1, 3, 1, 8, 2, 1, 3, 2, 5, 1, 2, 0, 0, 0, 0], #37
                        ])
# print(np.array(horariosDePico[1]).ravel())

distribuicaoPassageiros = np.zeros((38, 24))
# print(distribuicaoPassageiros)

for ponto in range(len(Y)):
    vetor = np.array(horariosDePico[ponto]).ravel()
    somaHP = sum(vetor)
    Y = np.array([vetor[0]])
    for i in range(1, 24):
        aux = np.array([Y[i - 1] + vetor[i]])
        Y = np.append(Y, aux)
    # print(Y)
    # print(somaHP)

    for p in range(int(passageiros[ponto])):
        pos = random.randint(0, somaHP)
        for v in range(24):
            if pos <= Y[v] and pos > Y[v - 1]:
                distribuicaoPassageiros[ponto, v] += 1

#
# for i in range(2, 10):
#     x = np.random.chisquare(i,4)
#
#     print(x)

# print(distribuicaoPassageiros)
# for t in range(len(distribuicaoPassageiros)):
#     distribuicaoPassageiros[t, 5] += distribuicaoPassageiros[t, 0]
#     distribuicaoPassageiros[t, 0] = 0
# print('*')
print(distribuicaoPassageiros)


def devolveDestino(pontoAtual, horario):
    d = 0
    if(horario <=9):
        print("pegou do 1")
        return 38 - int(random.choice(listFinal1)/(4/(38-pontoAtual)))
    if(horario > 8 and horario <=13):
        print("pegou do 2")
        return 38 - int(random.choice(listFinal2)/(16/(38-pontoAtual)))

    if(horario > 13):
        print("pegou do 3")
        return 38 - int(random.choice(listFinal2)/(20/(38-pontoAtual)))
    return 38


import matplotlib.pyplot as plt
pont1 = np.random.noncentral_chisquare(0.3, .00010,size=1000000)
pont2 = np.random.noncentral_chisquare(4.5, .00010,size=1000000)
pont3 = np.random.noncentral_chisquare(7.5, .00010,size=1000000)
values = plt.hist(pont1, bins=200, density=True, color='crimson')
plt.show()

listFinal1 = [i for i in pont1 if i < 4]
listFinal2 = [i for i in pont2 if i < 16]
listFinal3 = [i for i in pont3 if i < 20]

unidade = 15 #quantas unidades por minuto

# print(listFinal)
print(devolveDestino(5, 6.9))

saida = open('/home/ubuntu/Documents/ESI_SYNC_DB_RECOMENDATION/ESI_WRF/passageiros1.txt', 'w+')

print('horario\tchegada\tdestino')

for i in range(38):
    ponto = np.array(distribuicaoPassageiros[i]).ravel()
    print(ponto)
    for auxHorario in range(len(ponto)):
        print(auxHorario)
        for d in range(int(ponto[auxHorario])):
            horarioDeChegada = random.uniform(auxHorario*60*unidade, (1.0+auxHorario)*60*unidade)
            d = devolveDestino(i, auxHorario)
            if(d <= i):
                print("deu ruim")
                saida.close()
            if int(horarioDeChegada) < 3600 or int(horarioDeChegada) > 18000:
                print('ai')
            s = str(int(horarioDeChegada)) + ';'+str(i)+';'+str(d)
            print(s)
            saida.write(s+'\n')

saida.close()

# fazer gerador de onibus e pontos
# max = 23*60*unidade

# saidaOnibus = open('/home/maxtelll/Documents/USP/sextoSemestre/rp2/onibus.txt', 'w+')
# saidaEntrePontos = open('/home/maxtelll/Documents/USP/sextoSemestre/rp2/temposEntrePontos.txt', 'w+')
# saidaParadas = open('/home/maxtelll/Documents/USP/sextoSemestre/rp2/temposParadas.txt', 'w+')
# for _ in range(10):
#     t = random.randint(10, 10*unidade)
#     saidaParadas.write(str(t)+'\n')

# saidaParadas.close()


# for novoOnibus in range(60):
#     inicio = random.randint(*novoOnibus*max/64, max)



# import scipy.optimize
#
# def parabola(x, a, b, c):
#     return a*x**2 + b*x + c
#
# params = [1, -5, 10]
# x = np.linspace(-5, 5, 31)
# y = parabola(x, params[0], params[1], params[2])
# plt.plot(x, y, label='analytical')
# plt.legend(loc='lower right')
# # plt.show()
#
# r = np.random.RandomState(42)
# y_with_errors = y + r.uniform(-1, 1, y.size)
# plt.plot(x, y_with_errors, label='sample')
# plt.legend(loc='lower right')
# plt.show()
