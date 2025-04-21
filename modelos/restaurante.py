from modelos.avaliacao import Avaliacao

class Restaurante:
    """
    Classe que representa um restaurante."""
    restaurantes = []
    def __init__(self, nome, categoria):
        """
        Inicializa um novo restaurante com nome e categoria.
        :param nome: Nome do restaurante.
        :param categoria: Categoria do restaurante.
        """
    
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._menu = []
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """"
        Retorna uma representação em string do restaurante."""
        return f"{self.nome} ({self.categoria}) "
    
    @property # a forma como o atributo é apresentado
    def ativo(self):
        """
        Retorna o status do restaurante (ativo ou inativo).
        :return: '☒' se o restaurante estiver ativo, '☐' caso contrário.
        """
        return '☒' if self._ativo else '☐'
    
    def alternar_ativo(self):
        """
        Alterna o status do restaurante entre ativo e inativo."""
        self._ativo = not self._ativo
    
    def adicionar_item_menu(self, item):
        """"
        Adiciona um item ao menu do restaurante.
        """
        self._menu.append(item)
    
    def receber_avaliacao(self, cliente, nota, comentario):
        """
        Recebe uma avaliação de um cliente.
        :param cliente: Nome do cliente que fez a avaliação.
        :param nota: Nota dada pelo cliente (de 0 a 5).
        :param comentario: Comentário do cliente sobre o restaurante.
        """
        avaliacao = Avaliacao(cliente, nota, comentario)
        self._avaliacoes.append(avaliacao)
    
    @property # é quando eu quero que uma função se comporte como um atributo
    def media_avaliacoes(self):
        """
        Calcula a média das avaliações do restaurante.
        :return: Média das notas das avaliações (de 0 a 5).
        """
        if not self._avaliacoes:
            return "Sem avaliações"
        elif len(self._avaliacoes) == 1:
            return self._avaliacoes[0].nota
        soma = sum(avaliacao.nota for avaliacao in self._avaliacoes)
        return round(soma / len(self._avaliacoes), 1)
    
    @classmethod
    def listar_restaurantes(cls):
        """
        Lista todos os restaurantes cadastrados."""
        for restaurante in cls.restaurantes:
            print(f"Nome: {restaurante._nome.ljust(10)}, Categoria: {restaurante._categoria.ljust(10)} - Ativo: {restaurante.ativo.ljust(10)}, Média: {str(restaurante.media_avaliacoes).ljust(10)}")

restaurante = Restaurante("la Mafia", "Italiana")
restaurante.alternar_ativo()
restaurante.adicionar_item_menu("Pizza")
restaurante.adicionar_item_menu("Macarrão")
novoRestaurante = Restaurante("sushi", "Japonesa")
novoRestaurante.adicionar_item_menu("Sushi")
Restaurante.listar_restaurantes()




