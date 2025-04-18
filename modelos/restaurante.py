class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._menu = []
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
    
    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f"Nome: {restaurante._nome.ljust(10)}, Categoria: {restaurante._categoria} - Ativo: {restaurante.ativo}")

restaurante = Restaurante("la Mafia", "Italiana")
restaurante.alternar_ativo()
restaurante.adicionar_item_menu("Pizza")
restaurante.adicionar_item_menu("Macarrão")
novoRestaurante = Restaurante("sushi", "Japonesa")
novoRestaurante.adicionar_item_menu("Sushi")
Restaurante.listar_restaurantes()




