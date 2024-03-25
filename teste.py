from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


restaurante_praca = Restaurante("Sal", "Brasileiro")
bebida_suco = Bebida("Suco de melancia", 5.0, 'grande')
prato_paozinho = Prato("Paozinho", 2.0, "O melhor pão da cidade")
restaurante_praca.adicionar_prato_no_cardapio(bebida_suco)
restaurante_praca.adicionar_prato_no_cardapio(prato_paozinho)



def main():
    print(bebida_suco)
    print(prato_paozinho)


if __name__ == '__main__':
    main()