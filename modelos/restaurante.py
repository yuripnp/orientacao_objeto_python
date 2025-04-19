from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._menu = []
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self.nome} ({self.categoria}) "
    
    @property # a forma como o atributo é apresentado
    def ativo(self):
        return '☒' if self._ativo else '☐'
    
    def alternar_ativo(self):
        self._ativo = not self._ativo
    
    def adicionar_item_menu(self, item):
        self._menu.append(item)
    
    def receber_avaliacao(self, cliente, nota, comentario):
        avaliacao = Avaliacao(cliente, nota, comentario)
        self._avaliacoes.append(avaliacao)
    
    @property # é quando eu quero que uma função se comporte como um atributo
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return "Sem avaliações"
        elif len(self._avaliacoes) == 1:
            return self._avaliacoes[0].nota
        soma = sum(avaliacao.nota for avaliacao in self._avaliacoes)
        return round(soma / len(self._avaliacoes), 1)
    
    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f"Nome: {restaurante._nome.ljust(10)}, Categoria: {restaurante._categoria.ljust(10)} - Ativo: {restaurante.ativo.ljust(10)}, Média: {str(restaurante.media_avaliacoes).ljust(10)}")

restaurante = Restaurante("la Mafia", "Italiana")
restaurante.alternar_ativo()
restaurante.adicionar_item_menu("Pizza")
restaurante.adicionar_item_menu("Macarrão")
novoRestaurante = Restaurante("sushi", "Japonesa")
novoRestaurante.adicionar_item_menu("Sushi")
Restaurante.listar_restaurantes()




