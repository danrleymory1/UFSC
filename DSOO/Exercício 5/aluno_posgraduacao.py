from aluno import Aluno


class AlunoPosGraduacao(Aluno):
    def __init__(self, cpf, dias_de_emprestimo, matricula):
        super().__init__(cpf, dias_de_emprestimo, matricula)
        self.__elaborando_tese = False

    @property
    def elaborando_tese(self):
        return self.__elaborando_tese

    @elaborando_tese.setter
    def elaborando_tese(self, elaborando_tese):
        self.__elaborando_tese = elaborando_tese

    def emprestar(self, titulo_livro):
        if self.__elaborando_tese:
            return f'Aluno de matricula "{self.matricula}" pegou emprestado o livro: {titulo_livro} com {2 * self.dias_de_emprestimo} dias de prazo'
        else:
            return f'Aluno de matricula "{self.matricula}" pegou emprestado o livro: {titulo_livro} com {self.dias_de_emprestimo} dias de prazo'
