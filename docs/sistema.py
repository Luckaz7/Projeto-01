from docs.lib.estrutura import *
from time import sleep

criar_tabela()

while True:
    opcao = menu(['Cadastrar pessoa', 'Mostrar pessoas cadastradas', 'Atualizar dados', 'Excluir pessoa', 'Sair'])
    if opcao == 1:
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        telefone = leiaInt('DDD + Telefone: ')
        cadastrar_pessoa(nome, idade, telefone)
    elif opcao == 2:
        listar_pessoas()
    elif opcao == 3:
        listar_pessoas()
        id = leiaInt('Digite o ID da pessoa a ser atualizada: ')
        novo_nome = str(input('Novo nome: '))
        nova_idade = leiaInt('Nova idade: ')
        atualizar_pessoa(id, novo_nome, nova_idade)
    elif opcao == 4:
        listar_pessoas()
        id = leiaInt('Digite o ID da pessoa a ser excluida: ')
        excluir_pessoa(id)
    elif opcao == 5:
        cabecalho('Encerrando o sistema...Até logo!')
        break
    else:
        print('Opção inválida! Tente novamente.\n')
    sleep(2)
