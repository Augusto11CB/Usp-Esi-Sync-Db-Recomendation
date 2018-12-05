import sys
class Busca():
    global busca
    global max_price
    global min_price
    global categoria
    global ordenacao
    global id_cliente

    def __init__(self):
        self.busca = None
        self.max_price = sys.maxsize
        self.min_price = 0
        self.categoria = None
        self.ordenacao = None
        self.id_cliente = None

    def atribui_valor_maximo(self, vm):
        self.max_price = vm

    def atribui_valor_minimo(self, vm):
        self.min_price = vm

    def atribui_busca(self, b):
        self.busca = b

    def atribui_ordenacao(self, od):
        self.ordenacao = od

    def atribui_categoria(self, cat):
        self.categoria = cat

    def atribui_id(self, idc):
        self.id_cliente = idc
