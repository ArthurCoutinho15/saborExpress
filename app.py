import os

restaurantes = [{'nome': 'Sal', 'categoria':'Italiano', 'ativo':False},
                {'nome': 'Praça', 'categoria':'Pizza', 'ativo':True},
                {'nome': 'Cantina', 'categoria':'Brasileira', 'ativo':False}
]

def exibir_nome_programa():
    """ Exibe o nome do programa """
    print("Sabor express\n")

def exibir_opcoes():
    """ Exibe as opções disponíveis no menu principal """
    print(" 1. Cadastrar restaurante\n 2. Listar restaurante\n 3. Alternar estado do restaurante\n 4. Sair")

def finalizar_app():
    """ Exibe mensagem de finalização do aplicativo """
    exibir_subtitulos("Finalizando o app\n")

def voltar_menu():
    """ Solicita uma tecla para voltar ao menu principal

        Outputs:
        - Retorna ao menu principal
    """
    input("Digite qualquer tecla para voltar ao menu principal\n")
    main()

def opcao_invalida():
    """ Exibe mensagem de opção inválida e retorna oa menu principal """
    print("Opção inválida\n")
    voltar_menu()
 
def exibir_subtitulos(texto):
    """ Exibe um subtítulo estilizado na tela """
    os.system('cls')
    linha = "*" * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print(' ')

def cadastrar_restaurante():
    """ Essa função é responsável por cadastrar um novo restaurante 

        Inputs:
        - Nome do restaurante
        - Nome categoria

        Outputs:
        - Adiciona um novo restaurante a lista de restaurantes
        - 
        
    """
    exibir_subtitulos("Cadastro de novos restaurantes\n")
    nome_restaurante = input("Nome do restaurante: ")
    categoria = input(f"Categoria do restaurante {nome_restaurante}: ")
   
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_restaurante)

    print(f"Restaurante {nome_restaurante} cadastrado com sucesso")
    voltar_menu()

def listar_restaurante():
    ''' Lista os restaurantes presentes na lista 
    
        Outputs:
        - Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulos("Listagem de restaurantes:")

    print(f"{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status" )

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = "Ativado" if restaurante['ativo'] else "Desativado"
        print(f'.{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    print(' ')
    voltar_menu()

def alternar_estado_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulos("Alterando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if(nome_restaurante == restaurante['nome']):
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'Restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if(not restaurante_encontrado):
        print(f"O restaurante {nome_restaurante} não foi encontrado")
    voltar_menu()

def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        escolha = int(input("Escolha uma opção: ")) 
        if escolha == 1:
            print("Cadastrar restaurante\n")
            cadastrar_restaurante()
        elif escolha == 2:
            print("Listar restaurante")
            listar_restaurante()
        elif escolha == 3:
           alternar_estado_restaurante()
        elif escolha == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()


def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()


if (__name__ == '__main__'):
    main()
 