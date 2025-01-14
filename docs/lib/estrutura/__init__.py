import os.path

from docs.lib.interface import *
import json


def cadastrar_pessoa(pessoas):
    """
    -> Função para cadastrar pessoas.
    :param pessoas: variável que contem um arquivo vazio em formato .JSON
    """
    try:
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        telefone = leiaInt('DDD + Telefone: ')
        pessoas[nome] = {'idade': idade, 'Telefone': telefone}
    except Exception as e:
        print(f'Houve um problema no cadastro: {e}!')
    else:
        print(f'Pessoa {nome} cadastrada com sucesso!\n')


def salvar_pessoa(pessoas, arquivo='pessoas.json'):
    """
    -> Função para salvar no arquivo .JSON as pessoas cadastradas na função cadastrar_pessoas.
    :param pessoas: pessoas cadastradas.
    :param arquivo: arquivo .JSON que armazena os dados da pessoa cadastrada.
    """
    try:
        with open(arquivo, 'w') as f:
            json.dump(pessoas, f, indent=4)
    except IOError as e:
        print(f'Houve um problema no salvamento dos dados!: {e}')
    else:
        print('Dados salvos com sucesso!')


def carregar_pessoas(arquivo='pessoas.json'):
    """
    -> Função para carregar e mostrar as pessoas cadastradas e armazenadas no arquivo .JSON
    :param arquivo: arquivo .JSON utilizado para armazenas as pessoas cadastradas.
    :return: retorna o arquivo criado com o seu conteúdo dentro(se houve), se não, cria um novo vazio.
    """
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print('Arquivo não encontrado! Criando novo cadastro.')
        return {}
    except json.JSONDecodeError as e:
        print(f'Erro ao carregar os dados: {e}')
        return {}


def limpar_dados(arquivo='pessoas.json'):
    try:
        if os.path.exists(arquivo):
            with open(arquivo, 'w') as f:
                json.dump({}, f, indent=4)
            print('Todos os registros foram deletados com sucesso!')
        else:
            print('Nenhum arquivo encotrado para limpar')
    except Exception as e:
        print(f'Ocorreu um erro ao limpar os dados: {e}')

