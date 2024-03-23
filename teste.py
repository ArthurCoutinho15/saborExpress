from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("Praça", "Italiano")
restaurante_praca.receber_avaliacao('Arthur', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Julia', 5)


def main():
    Restaurante.listar_restaurantes()



if __name__ == '__main__':
    main()