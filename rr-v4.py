def rr(processos, quantum):
    array_de_pronto = processos
    qtd_processos_prontos = len(array_de_pronto)
    while (qtd_processos_prontos > 0):
        # print(array_de_pronto)
        array_de_pronto = deduz(array_de_pronto, quantum)
        qtd_processos_prontos -= 1


def deduz(array, q):
    print(f"Array recebido {array}")
    novo_array = []
    valor = 0
    for item in array:
        if item <= q:
            valor -= item
        else:
            valor = item - q
        # valor = 0 apenas pra aparecer na tabela
        if valor < 0:
            valor = 0
            novo_array.append(valor)
        else:
            novo_array.append(valor)
        # if valor > 0:
        #     novo_array.append(valor)
    print(f"Array de saida {novo_array}")
    return novo_array


if __name__ == '__main__':
    processos = [40, 20, 50, 30]
    # processos = [40, 40]
    quantum = 20
    troca_contexto = 5
    rr(processos, quantum)