my_set = {3,4,5}

empty_set = {}
print(type(empty_set))

empty_set = set()
print(type(empty_set))

# Son una forma de obtener un conjunto de datos inmutable y único

# Borrar un elemento especifico, si no lo encuentra devuelve el mismo set.
my_set.discard(3)

# Borrar un elemento especifico, si no lo encuentra devuelve error.
my_set.remove(3)

# Borrar un elemento aleatorio
my_set.pop()

# Borrar todos los elementos
my_set.clear()