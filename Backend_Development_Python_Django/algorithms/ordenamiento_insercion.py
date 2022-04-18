import random

def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):
        posicion_actual = indice
        valor_actual = lista[indice]
        print(f"Iterador: {posicion_actual} --- Valor: {valor_actual}")
        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            print(f"Comparando {valor_actual} con {lista[posicion_actual - 1]}")
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1
            print(lista)
        lista[posicion_actual] = valor_actual
    return lista


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    # lista = [5,4,3,2,1]
    print(f'Mi lista desordenada: {lista}')
    lista_ordenada = ordenamiento_por_insercion(lista)
    print(lista_ordenada)