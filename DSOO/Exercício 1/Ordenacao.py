"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""

class Ordenacao():

    def __init__(self, array_para_ordenar:[]):
        """Recebe o array com o conteudo a ser ordenado"""
        self.lista = array_para_ordenar

    def ordena(self):
        """Realiza a ordenacao do conteudo do array recebido no construtor"""
        for i in range(len(self.lista)):
            for j in range(len(self.lista)-i-1):
                if self.lista[j] > self.lista[j+1]:
                    self.lista[j], self.lista[j+1] = self.lista[j+1], self.lista[j] 
                    """Linha 17 Duvida: tentei várias vezes em linhas separadas, mas não roda normal. 
                    Depurei, porém não entendi como se faz a troca normal em um mas em outro não"""

    def to_string(self):
        """Converte o conteudo do array em String formatado
           Exemplo: 
           Para o conteudo do array: [1,2,3,4,5]
           Retorna: "1,2,3,4,5"
           @return String com o conteudo do array formatado
     """
        frase_lista = ''
        for i in range(len(self.lista)):
            if i == 0:
                frase_lista = frase_lista+str(self.lista[i])
            else:
                frase_lista = frase_lista+','+str(self.lista[i])
        return frase_lista