def rr(processos, quantum):
    array_de_pronto = processos
    qtd_processos_prontos = len(array_de_pronto)
    novo_array = []
    while (qtd_processos_prontos > 0):
        valor = 0
        for item in processos:
            if item <= quantum:
                valor -= item
            else:
                valor = item - quantum
            # valor = 0 apenas pra aparecer na tabela
            if valor < 0:
                valor = 0
                novo_array.append(valor)
            else:
                novo_array.append(valor)
        print(f"Array de saida {novo_array}")
        qtd_processos_prontos -= 1
        1 = []


if __name__ == '__main__':
    processos = [40, 20, 50, 30]
    # processos = [40, 40]
    quantum = 20
    troca_contexto = 5
    rr(processos, quantum)