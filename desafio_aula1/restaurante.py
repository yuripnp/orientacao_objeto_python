class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    def __str__(self):
        return self.nome
    
lamafia = Restaurante("La Mafia", "Italiana")
print(f"Nome: {lamafia.nome}")
print(f"Categoria: {lamafia.categoria}")
print(vars(lamafia))
print(dir(lamafia))
