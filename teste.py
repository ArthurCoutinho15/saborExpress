from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa


restaurante_praca = Restaurante("Sal", "Brasileiro")
bebida_suco = Bebida("Suco de melancia", 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato("Paozinho", 2.0, "O melhor pão da cidade")
prato_paozinho.aplicar_desconto()
prato_sobremesa = Sobremesa("Panacotta", 35.0, "Morango", "Grande")
prato_sobremesa.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(prato_sobremesa)


def main():
    restaurante_praca.exibir_cardapio()

if __name__ == '__main__':
    main()