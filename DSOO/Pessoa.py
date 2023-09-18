class Pessoa:
    all = []
    def __init__(self, nome, telefone, cidade:Endereco, estado:Endereco):
        self.__nome = nome
        self.__telefone = telefone
        self.__endereco = (Endereco(cidade, estado))
