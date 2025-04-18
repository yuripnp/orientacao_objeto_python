class Carro:
    def __init__(self, cor, modelo, ano):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return f"Carro(cor={self.cor}, modelo={self.modelo}, ano={self.ano})"