

def wordParser(sentence):

    word_array = sentence.split(' ')
    final_fix_string = ''
    
    for word in word_array:
        counter = 0
        special_characters = '.;-!'
        fixed_string=''
        distinct_characters=''
        character_exists = False
        for letter in word:
            if letter in special_characters:
                character_exists = True
                character = letter
            
            if letter not in distinct_characters:
                distinct_characters+=letter

            counter +=1

        first_letter = word[0]
        if character_exists:
            info_array = distinct_characters.split(character)
            if info_array[1] != '':
                lenght_first = '' if len(info_array[0])-2 == 0 else len(info_array[0])-2
                last_letter = info_array[0][len(info_array[0])-1]
                first_letter_after_character = info_array[1][0]
                lenght_second = '' if len(info_array[1])-2 == 0 else len(info_array[1])-2
                last_letter_after_character = info_array[1][len(info_array[1])-1]
                fixed_string += first_letter + str(lenght_first) + last_letter + character + first_letter_after_character + str(lenght_second) + last_letter_after_character + ' '
                final_fix_string += fixed_string
            else:
                lenght_first = '' if len(info_array[0])-2 == 0 else len(info_array[0])-2
                last_letter = info_array[0][len(info_array[0])-1]
                fixed_string += first_letter + str(lenght_first) + last_letter + character + ' '
                final_fix_string += fixed_string
        else:
            lenght_first = '' if len(distinct_characters) - 2 == 0 else len(distinct_characters) - 2
            last_letter = word[-1]
            fixed_string += first_letter + str(lenght_first) + last_letter + ' '
            final_fix_string += fixed_string

    print(final_fix_string)

def run():
    sentence = 'El contenido está alineado con los objetivos de mi compañía'
    print(len(sentence))
    # wordParser(sentence)


if __name__ == '__main__':
    run()