from projeto2.lib.interface import *
import json


def cadastrar_pessoa(pessoas):
    try:
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        pessoas[nome] = {'idade': idade}
    except Exception as e:
        print(f'Houve um problema no cadastro: {e}!')
    else:
        print(f'Pessoa {nome} cadastrada com sucesso!\n')


def salvar_pessoa(pessoas, arquivo='pessoas.json'):
    try:
        with open(arquivo, 'w') as f:
            json.dump(pessoas, f, indent=4)
    except IOError as e:
        print(f'Houve um problema no salvamento dos dados!: {e}')
    else:
        print('Dados salvos com sucesso!')


def carregar_pessoas(arquivo='pessoas.json'):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print('Arquivo não encontrado! Criando novo cadastro.')
        return {}
    except json.JSONDecodeError as e:
        print(f'Erro ao carregar os dados: {e}')
        return {}
