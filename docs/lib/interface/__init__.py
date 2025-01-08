def leiaInt(txt):
    """
    -> Função que faz uma verificação se o número informado é do tipo inteiro. :param txt: texto ou valor informado
    pelo usuário :return: retorna o valor se for do tipo inteiro, ou caso contrário, retorna o erro ou uma informação
    de que o usuário não informou nenum dado.
    """
    try:
        numero = int(input(txt))
    except (ValueError, TypeError):
        print('Informe um valor do tipo inteiro válido!')
    except KeyboardInterrupt:
        print('O usuário preferiu não informar nenhum dado!')
        return 0
    else:
        return numero


def linha(tam=42):
    """
    -> Função para layout do sistema onde gera uma linha quando chamado.
    :param tam: recebe o tamanho da linha a ser gerada(por padrão foi colocado como 42).
    :return: retorna '-' * o tamanha da linha informado pelo usuário.
    """
    return '-' * tam


def cabeçalho(txt):
    """
    -> Função que gera um cabeçalho de texto quando chamada.
    :param txt: recebe um texto informado pelo usuário para ser utilizado como cabeçalho.
    """
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    """
    -> Função que gera um menu interativo com opções ao usuário.
    :param lista: lista com as opções a serem escolhidas pelo usuário.
    :return: retorna a opção informada pelo usuário.
    """
    cabeçalho('Menu principal')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc
