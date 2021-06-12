def rr(processos, quantum):
    array_de_pronto = processos
    qtd_processos_prontos = len(array_de_pronto)
    acc_time = 0
    while (qtd_processos_prontos > 0):
        novo_array = []
        # print(array_de_pronto)
        print(f"Array recebido {array_de_pronto}")
        valor = 0
        array_acc_time = []
        i = 0
        for item in array_de_pronto:
            if item <= quantum and item > 0:
                valor -= item
                acc_time += item  # TODO
                array_acc_time.append(acc_time)  # TODO
            else:
                valor = item - quantum
                acc_time += quantum  # TODO
                array_acc_time.append(acc_time)  # TODO

            # valor = 0 apenas pra aparecer na tabela
            if valor < 0:
                valor = 0
                novo_array.append(valor)
                # array_de_pronto[i] = valor
            else:
                novo_array.append(valor)
                array_de_pronto[i] = valor
            i += 1

        print(f"Array de saida {novo_array}")
        print(f"Tempo acumulado {acc_time}")
        print(f"Array de tempos {array_acc_time}")
        print(f"*" * 50)
        qtd_processos_prontos -= 1

if __name__ == '__main__':
    processos = [40, 20, 50, 30]
    # processos = [40, 40]
    quantum = 20
    troca_contexto = 5
    rr(processos, quantum)
