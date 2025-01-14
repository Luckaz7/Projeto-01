from docs.lib.estrutura import *
from docs.lib.interface import *
from time import sleep

pessoas = carregar_pessoas()

while True:
    resposta = menu(['Cadastrar Pessoa', 'Mostrar pessoas cadastradas', 'Limpar dados', 'Salvar e sair'])
    if resposta == 1:
        cadastrar_pessoa(pessoas)
    elif resposta == 2:
        if pessoas:
            cabecalho('Pessoas Cadastradas:')
            for nome, dados in pessoas.items():
                print(f"{nome:<13}{dados['idade']:>3} anos{dados['Telefone']:>20}")
        else:
            print('Nenhuma pessoa cadastrada.')
        print()
    elif resposta == 3:
        limpar_dados()
        pessoas.clear()
    elif resposta == 4:
        salvar_pessoa(pessoas)
        print('Encerrando o sistema...Até logo!')
        break
    else:
        print('Opção inválida! Tente novamente.\n')
    sleep(2)
