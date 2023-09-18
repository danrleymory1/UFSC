class Produto:
    def __init__(self, codigo, descricao, categoria_produto, cliente="", quantidade=None, preco_unitario=None):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__categoria_produto = categoria_produto
        self.__cliente = cliente
        self.__quantidade = quantidade
        self.__preco_unitario = preco_unitario

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def categoria_produto(self):
        return self.__categoria_produto

    @categoria_produto.setter
    def categoria_produto(self, categoria_produto):
        self.__categoria_produto = categoria_produto

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    @property
    def preco_unitario(self):
        return self.__preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        self.__preco_unitario = preco_unitario

    def preco_total(self):
        return self.__preco_unitario * self.__quantidade
