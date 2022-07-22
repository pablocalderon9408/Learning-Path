# Union

my_set1 = {3,4,5}
my_set2 = {5,6,7}

my_set3 = my_set1 | my_set2
# Esto es lo que imprime: {3,4,5,6,7}
print(my_set3)


# Intersección
my_set1 = {3,4,5}
my_set2 = {5,6,7}

my_set3 = my_set1 & my_set2
# Esto es lo que imprime: {5}
print(my_set3)

# Diferencia: Toma un set de base y le quita lo que esté también en el otro.
my_set1 = {3,4,5}
my_set2 = {5,6,7}

my_set3 = my_set1 - my_set2
# Esto es lo que imprime: {3,4}
print(my_set3)

my_set4 = my_set2 - my_set1
# Esto es lo que imprime: {6,7}
print(my_set4)

# Diferencia simétrica
my_set1 = {3,4,5}
my_set2 = {5,6,7}

my_set3 = my_set1 ^ my_set2
# Esto es lo que imprime: {3,4,6,7}
print(my_set3)
