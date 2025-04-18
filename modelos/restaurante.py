class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        self.menu = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self.nome} ({self.categoria}) "
    
    @property # a forma como o atributo é apresentado
    def ativo(self):
        return '☒' if self._ativo else '☐'
    
    def adicionar_item_menu(self, item):
        self.menu.append(item)
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f"Nome: {restaurante.nome.ljust(10)}, Categoria: {restaurante.categoria} - Ativo: {restaurante.ativo}")

restaurante = Restaurante("La Mafia", "Italiana")
restaurante.adicionar_item_menu("Pizza")
restaurante.adicionar_item_menu("Macarrão")
Restaurante.listar_restaurantes()
novoRestaurante = Restaurante("Sushi", "Japonesa")
novoRestaurante.adicionar_item_menu("Sushi")
Restaurante.listar_restaurantes()




