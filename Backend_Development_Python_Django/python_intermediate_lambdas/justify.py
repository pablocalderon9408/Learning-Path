## ### Input

# - Un string de una sola linea
# - El ancho de la línea esperada

# Ninguna palabra del string será más larga que el ancho de línea esperado.

### Output

# Mostrar por standard output el texto justificado, de acuerdo a las siguientes reglas:
# 
# - Use espacios para separar las palabras
# - Cada línea deberá contener la mayor cantidad de palabras posibles
# - Usar \n para separar líneas
# - El máximo y el mínimo gap de una misma fila no puede diferir en más de 1 espacio
#     - Incorrecto: Lorem-----ipsum--dolor
#     - Correcto: Lorem----ipsum---dolor
# - Las líneas deberán terminar en una palabra, no un espacio
# - '\n' no está incluido en el largo de una línea
# - Espacios más largos van primero, luego los espacios más pequeños.
#     - Correcto: 'Lorem---ipsum---dolor--sit--amet' (3, 3, 2, 2 espacios).
#     - Incorrecto: 'Lorem--ipsum--dolor---sit---amet' (2, 2, 3, 3 espacios).
# - La última línea no estará justificada, sólo un espacio entre palabras
# - Líneas con una sola palabra larga no necesitan espacios ('unapalabralarga\n').

### Input:


# La historia de la ópera tiene una duración relativamente corta dentro del contexto de la historia de la música en general apareció en 1597, fecha en que se creó la primera ópera.

# La  historia de la ópera tiene
# una   duración   relativamente
# corta  dentro  del contexto de
# la  historia  de  la música en
# general   apareció   en  1597,
# fecha   en   que  se  creó  la
# primera ópera.

# Una función solo para devolver 2 strings: el de 30 caracteres y el restante.
def add_spaces(corrupt_line, spaces_to_add):
    list_of_words = corrupt_line.split(" ")
    available_spaces = len(list_of_words) - 1
    last_word = list_of_words.pop()
    space = " "
    new_string = ""
    counter = 1
    itera = 0
    while spaces_to_add>0:
        if counter >= (available_spaces)*2:
            counter = 1
            itera += 1
        list_of_words.insert(counter+itera, space)
        counter += 2
        spaces_to_add -= 1
    for word in list_of_words:
        new_string+=word
        if word is not space:
            new_string+=space
    new_string += last_word
    return new_string

def split_string(string_to_justifiy, line_length, result_text=""):
    if len(string_to_justifiy)>line_length:
        if string_to_justifiy[0] == " ":
            string_to_analize = string_to_justifiy[1:line_length+1]
            string_left = string_to_justifiy[line_length+1:]
        else:
            string_to_analize = string_to_justifiy[0:line_length]
            string_left = string_to_justifiy[line_length:]
        string_to_reverse = string_to_analize
        reversed_string = string_to_reverse[::-1]
        last_space = len(reversed_string) - reversed_string.index(" ") - 1
        line = string_to_reverse[0:last_space]
        spaces_to_add = line_length - len(line)
        # import ipdb ; ipdb.set_trace()
        improved_line = add_spaces(line, spaces_to_add)
        # Mejorar los espacios de la linea corrupta.
        remanent = string_to_reverse[last_space:]
        result_text += improved_line + "\n"
        string_left = remanent + string_left
        return split_string(
            string_to_justifiy=string_left,
            line_length=line_length, 
            result_text=result_text, 
            )
    else:
        if string_to_justifiy[0] == " ":
            line = string_to_justifiy[1:]
            result_text += line
        else:
            result_text += string_to_justifiy
    return result_text

if __name__ == '__main__':
    string_to_justifiy = "La historia de la ópera tiene una duración relativamente corta dentro del contexto de la historia de la música en general apareció en 1597, fecha en que se creó la primera ópera." 
    line_length = 30
    result = split_string(string_to_justifiy, line_length)
    print(result)