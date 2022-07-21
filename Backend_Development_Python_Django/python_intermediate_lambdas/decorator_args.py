def tipo_encantamiento(tipo):
    def objeto_encantado(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            print(f"Reforzada con encantamiento de tipo {tipo}")
            for category in args:
                print("{:<8} {:<20}".format(category, "+20"))
        return wrapper
    return objeto_encantado

@tipo_encantamiento("Fuego")
def arma(fp):
    print("espada de cola de dragón")
    
@tipo_encantamiento("cristal mágico")
def escudo(fp, hp, dp):
    print("escudo de hierba")

arma("100")
escudo("20", "30", "80")