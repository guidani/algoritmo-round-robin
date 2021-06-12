def rr(processos, quantum):
    array_de_pronto = processos
    qtd_processos_prontos = len(array_de_pronto)
    while (qtd_processos_prontos > 0):
        # print(array_de_pronto)
        array_de_pronto = deduz(array_de_pronto, quantum)
        qtd_processos_prontos -= 1


def deduz(processos, quantum):
    print(f"Array recebido {processos}")
    novo_array = []
    valor = 0
    acc_time = 0
    array_acc_time = []
    for item in processos:
        if item <= quantum:
            valor -= item
            acc_time += item # TODO
            array_acc_time.append(acc_time) # TODO
        else:
            valor = item - quantum
            acc_time += quantum # TODO
            array_acc_time.append(acc_time) # TODO
        # valor = 0 apenas pra aparecer na tabela
        if valor < 0:
            valor = 0
            novo_array.append(valor)
        else:
            novo_array.append(valor)
        # if valor > 0:
        #     novo_array.append(valor)
    print(f"Array de saida {novo_array}")
    print(f"Tempo acumulado {acc_time}")
    print(f"Array de tempos {array_acc_time}")
    print(f"*"*50)
    return novo_array


if __name__ == '__main__':
    processos = [40, 20, 50, 30]
    # processos = [40, 40]
    quantum = 20
    troca_contexto = 5
    rr(processos, quantum)
