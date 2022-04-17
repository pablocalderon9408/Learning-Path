import random

def busqueda_lineal(lista,objetivo):
    match=False
    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    return match

if __name__ == '__main__':
    tamano_lista = int(random.randint(20,100))
    objetivo = int(input('# a encontrar: '))
    lista = [random.randint(0,100) for i in range(tamano_lista)]

    encontrado = busqueda_lineal(lista, objetivo)

    print(lista)
    print(f'{objetivo} {"está" if encontrado else "no está"} en la lista')