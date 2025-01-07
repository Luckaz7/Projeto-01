def leiaInt(txt):
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
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('Menu principal')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc
