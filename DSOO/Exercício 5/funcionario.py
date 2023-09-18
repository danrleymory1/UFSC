from abc import ABC, abstractmethod
from usuario_bu import UsuarioBU


class Funcionario(UsuarioBU, ABC):
    @abstractmethod
    def __init__(self, departamento, cpf, dias_de_emprestimo):
        super().__init__(cpf, dias_de_emprestimo)
        self.__departamento = departamento

    @property
    def departamento(self):
        return self.__departamento

    @departamento.setter
    def departamento(self, departamento):
        self.__departamento = departamento

    def emprestar(self, titulo_livro):
        return f'do departamento "{self.departamento}" pegou emprestado o livro: {titulo_livro} com {self.dias_de_emprestimo} dias de prazo'        

    def devolver(self, titulo_livro):
        return f'do departamento "{self.departamento}" devolveu o livro: {titulo_livro}'
