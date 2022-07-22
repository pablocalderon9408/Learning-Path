def remover_duplicados(lista):
    return print(list(set(lista)))

def run():
    lista = [1,1,4,4,5,6,4,2,4,5,5,6,4,1,56,8,9,0,0,7,3,3]
    remover_duplicados(lista)

if __name__ == "__main__":
    run()
