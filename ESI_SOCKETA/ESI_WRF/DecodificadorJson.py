from Interface import Interface
from Busca import Busca

class InterfaceJson():
    global interface
    def __init__(self):
        self.interface = Interface()

    def decodifica_requisicao_busca(self, pedido):
        busca, categoria, min_price, max_price, ordenacao = pedido.split(',')
        if not busca:
            busca = None
        if not min_price:
            min_price = None

        if not max_price:
            max_price = None

        if not categoria:
            categoria = None

        if not ordenacao:
            ordenacao = None

        b = Busca()
        b.atribui_valor_minimo(min_price)
        b.atribui_valor_maximo(max_price)
        b.atribui_busca(busca)
        b.atribui_ordenacao(ordenacao)
        b.atribui_categoria(categoria)
        return self._codifica_lista(self.interface.busque(b))


    def _codifica_lista(self, lista):
        return ','.join(str(l) for l in lista)


    def decodifica_requisicao_atualizacao(self, requisicao):
        # insercao<|>atualizacao<|>delecao
        # split no <|>
        # insercao:insercao1(*)insercao2(*)insercao3.....
        # em uma insercao:
        pass






