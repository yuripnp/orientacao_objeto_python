from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("Praça", "Paraense")
restaurante_mexicana = Restaurante("Mexicana", "Mexicana")
restaurante_brasileira = Restaurante("Brasileira", "Brasileira")

restaurante_brasileira.receber_avaliacao("João", 5, "Muito bom")
restaurante_brasileira.receber_avaliacao("Maria", 4, "Bom")
restaurante_praca.alternar_ativo()

Restaurante.listar_restaurantes()


def main():
    pass

if __name__ == "__main__":
    main()