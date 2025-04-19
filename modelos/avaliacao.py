class Avaliacao:
    def __init__(self, cliente, nota, comentario):
        self.cliente = cliente
        if nota < 0 or nota > 5:
            raise ValueError("Nota deve estar entre 0 e 5.")
        else:
            self.nota = nota
        self.comentario = comentario
