from random import randint

def gera_cnpj_incompleto():
    primeiro_dig = randint(0, 9)
    segundo_dig = randint(0, 9)
    segundo_bloco = randint(100, 999)
    terceiro_bloco = randint(100, 999)
    quarto_bloco = '0001'
    semi = str(primeiro_dig) + str(segundo_dig) + '.' + str(segundo_bloco) + '.' + str(
        terceiro_bloco) + '/' + quarto_bloco
    cnpj = semi
    v_num = []
    for valor in cnpj:
        if valor.isnumeric():
            v_num.append(valor)
    aux = 6
    cont = 1
    lista = []
    while True:
        if cont > 12:
            break
        else:
            if aux == 2:
                aux = 10
            aux -= 1
            lista.append(aux)
            cont += 1

    calc = [(int(x) * y) for x,y in zip(v_num, lista)]
    soma = 0
    for valor in calc:
        soma += valor
    form = 11 - (soma % 11)
    if form > 9:
        form = 0
    print(f'digt1 - {form}')
    print(f'cnpj gerado {cnpj}')
    v_num.append(str(form))
    return v_num


def Valida_cnpj():
    cnpj = gera_cnpj_incompleto()
    v_num = []
    for valor in cnpj:
        if valor.isnumeric():
            v_num.append(valor)
    aux = 7
    cont = 1
    lista = []
    while True:
        if cont > 13:
            break
        else:
            if aux == 2:
                aux = 10
            aux -= 1
            lista.append(aux)
            cont += 1

    calc = [(int(x) * y) for x, y in zip(v_num, lista)]
    soma = 0
    for valor in calc:
        soma += valor
    form = 11 - (soma % 11)
    if form > 9:
        form = 0

    v_num.append(str(form))
    print(f'dig2 - {form}')
    novo_cnpj = ''
    for valor in v_num:
        novo_cnpj += valor
    print(novo_cnpj)
    return novo_cnpj




