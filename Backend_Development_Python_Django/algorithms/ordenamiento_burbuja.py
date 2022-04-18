import random

def ordenamiento_de_burbuja(lista):
    n = len(lista)

    """Loop to guarantee all the list will be cover."""
    for i in range(n):
        print(f'Iteración {i}')
        print(lista)
        """There is a guarantee that always the biggest number will be at the end. So It is not needed
        to go till the end in every loop. Therefore this loop is n - i - 1"""
        for iterator in range(0, n - i - 1): # O(n) * O(n) = O(n * n) = O(n**2)
            print(f'{lista[iterator]} -- VS -- {lista[iterator+1]}')
            if lista[iterator] > lista[iterator + 1]:
                lista[iterator], lista[iterator + 1] = lista[iterator + 1], lista[iterator]
            print(lista)

    return lista

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    # lista = [5,4,3,2,1]
    print(f'Mi lista desordenada: {lista}')
    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)