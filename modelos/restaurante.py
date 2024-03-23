from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)


    def __str__(self):
        return f'{self._nome.ljust(25)} | {self._categoria.ljust(25)} {self.ativo} '
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
       return '⌧ 'if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
 
    def receber_avaliacao(self, cliente, nota):
        if nota >= 0 and nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if(not self._avaliacao):
            return '-'
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        notas_qtd = len(self._avaliacao)
        media = round(soma / notas_qtd, 1)
        return media


