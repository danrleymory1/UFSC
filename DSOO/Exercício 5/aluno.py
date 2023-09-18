from abc import ABC, abstractmethod
from usuario_bu import UsuarioBU


class Aluno(UsuarioBU, ABC):
    @abstractmethod
    def __init__(self, cpf, dias_de_emprestimo, matricula):
        super().__init__(cpf, dias_de_emprestimo,)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
    
    @abstractmethod
    def emprestar(self, titulo_livro):
        pass

    def devolver(self, titulo_livro):
        return f'Aluno de matricula "{self.matricula}" devolveu o livro: {titulo_livro}'
