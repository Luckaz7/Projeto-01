from docs.lib.interface import *
import sqlite3


def conectar():
    return sqlite3.connect('cadastro.db')


def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY, 
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            telefone INTEGER NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()


def cadastrar_pessoa(nome, idade, telefone):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO pessoas (nome, idade, telefone) VALUES (?, ?, ?)", (nome, idade, telefone))
        conexao.commit()
        conexao.close()
        print(f'Pessoa {nome} cadastrada com sucesso!')
    except Exception as e:
        cabecalho(f'Erro ao cadastrar pessoa: {e}')


def listar_pessoas():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM pessoas')
        resultados = cursor.fetchall()
        conexao.close()

        if resultados:
            cabecalho('Pessoas cadastradas:')
            for pessoa in resultados:
                print(f'ID: {pessoa[0]}, Nome: {pessoa[1]}, Idade: {pessoa[2]}, Telefone: {pessoa[3]}')
        else:
            print('Nenhuma pessoa cadastrada.')
    except Exception as e:
        cabecalho(f'Erro ao listar pessoas: {e}')


def atualizar_pessoa(id, novo_nome, nova_idade):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute('UPDATE pessoas SET nome = ? WHERE id = ?', (novo_nome, nova_idade, id))
        conexao.commit()
        conexao.close()
        print('Dados atualizados com sucesso!')
    except Exception as e:
        print(f'Erro ao atualizar pessoa: {e}')


def excluir_pessoa(id):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM pessoas WHERE id = ?', (id,))
        conexao.commit()
        conexao.close()
        print('Pessoa excluída com sucesso.')
    except Exception as e:
        cabecalho(f'Erro ao excluir pessoa: {e}')
