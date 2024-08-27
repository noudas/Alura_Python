import os

restaurantes = [{'nome': 'Bobs Burger', 'categoria': 'Hamburger', 'ativo': False},
                {'nome': 'Japa Ines', 'categoria': 'Japones', 'ativo': True}]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
\n""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def voltar_ao_menu_principal():
    input("Digite uma tecla para voltar ao menu principal")
    main()

def exibir_sub_titulo(texto):
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def finalizar_app():
    exibir_sub_titulo('Encerrando o programa')

def opcao_invalida():
    print("Opcao Invalida\n")
    voltar_ao_menu_principal()

def cadastro_restaurante():
    cadastro = True
    while cadastro == True:
        exibir_sub_titulo('Cadastro de novos restaurantes')
        nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
        categoria = input('Digite a categoria do restaurante que deseja cadastrar: ')

        restaurantes.append({"nome": nome_do_restaurante, "categoria": categoria, "ativo": False})
        print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')
        valicadastro = input("Deseja continuar, Digite 'S' para continuar e 'N' para sair: ")
        if valicadastro.upper() == "S":

            continue
        else:
            cadastro = False
        
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_sub_titulo('Listar todos os restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurant in restaurantes:
        nome_res = restaurant["nome"]
        cat_res = restaurant["categoria"]
        ati_res = "Ativo" if restaurant["ativo"] == True else "Inativo"
        
        print(f"- {nome_res.ljust(20)} | {cat_res.ljust(20)} | {ati_res}")
    voltar_ao_menu_principal()

def alternar_estado_restaurante():

    def listar_restaurantes(ativo=True):
        os.system('cls')
        lista_nomes = [restaurant['nome'] for restaurant in restaurantes if restaurant.get('ativo') == ativo]
        if not lista_nomes:
            status = "ativos" if ativo else "desativados"
            print(f"Não há restaurantes {status}")
        else:
            print(lista_nomes)
        input("Digite uma tecla para voltar ao menu")
        alternar_estado_restaurante()

    def listar_ativos():
        listar_restaurantes(ativo=True)

    def listar_inativos():
        listar_restaurantes(ativo=False)

    def ativar_ou_desativar_restaurante():
        exibir_sub_titulo("Ativar ou Desativar um Restaurante")
        
        nome_restaurante = input("Digite o nome do restaurante que deseja alterar: ")
        for restaurant in restaurantes:
            if nome_restaurante == restaurant["nome"]:
                restaurant['ativo'] = not restaurant['ativo']
                status = "ativado" if restaurant['ativo'] else "desativado"
                print(f'O restaurante {nome_restaurante} foi {status} com sucesso.')
                input("Digite uma tecla para voltar ao menu")
                alternar_estado_restaurante()
        
        print(f"O restaurante {nome_restaurante} não foi encontrado.")
        input("Digite uma tecla para voltar ao menu")
        alternar_estado_restaurante()

    exibir_sub_titulo('Alterar o estado de algum Restaurante')
    
    try:
        ati_ina = int(input("""
Escolha uma opção: 
1. Listar Restaurantes Ativo
2. Listar Restaurantes Inativos
3. Ativar ou Desativar um restaurante
4. Voltar ao menu principal
"""))
    except ValueError:
        print("Use somente números.")
        return alternar_estado_restaurante()

    if ati_ina == 1:
        listar_ativos()

    elif ati_ina == 2:
        listar_inativos()

    elif ati_ina == 3:
        ativar_ou_desativar_restaurante()

    elif ati_ina == 4:
        voltar_ao_menu_principal()

    else:
        print("Opção inválida.")
        return alternar_estado_restaurante()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            print('Cadastrar restaurante')
            cadastro_restaurante()
        elif opcao_escolhida == 2:
            print('Listar restaurantes')
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurantes')
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()


if __name__ == '__main__':
    main()