import random

def busqueda_binaria(lista, comienzo, final, objetivo):
    
    if comienzo > final:
        return False

    medio = (comienzo + final) // 2
    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio+1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio-1, objetivo)


if __name__ == '__main__':
    tamano_lista = int(random.randint(20,100))
    objetivo = int(input('# a encontrar: '))
    lista = sorted([random.randint(0,100) for i in range(tamano_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)
    print(f'{objetivo} {"está" if encontrado else "no está"} en la lista')