def ricerca_binaria(lista, numero):
    inizio = 0
    fine = len(lista) - 1

    while inizio <= fine:
        medio = (inizio + fine) // 2
        if lista[medio] == numero:
            return True
        elif lista[medio] < numero:
            inizio = medio + 1
        else:
            fine = medio - 1

    return False