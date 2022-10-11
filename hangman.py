from random import choice
from color import colors


def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]


lst_fail = ['head',
            'body',
            'left arm',
            'right-arm', 'left-leg',
            'right-leg, you loose']  # declare a the list of human parts that the user lost in case of wrong estatment


dct = {"dudu": "long-hair",
       "thalison": "left-side",
       "biel": "beuty",
       "hads": "cow"}  # declare the names and the tips releted to the names inside a diconary, {"name": "tip"}

cont_error = 0  # count of errors
lst_hit = []  # declare a list that gonna be used the save the index of the corrent letters

dct_choice = choice(list(dct.items()))  # randomic select one of the items from the dicionariy, after changes to list
word_choice = dct_choice[0]  # the word selected to the game goint to be de index[0] of dct_choice
tip_choice = dct_choice[1]  # the tip selected to the game goint to be de index[1] of dct_choice


underline_choice = (len(word_choice) * '_')  # uses the len of word choice and multioplies to underlines


print('hangman GAME dude')
for c in range(len(word_choice) + 6):  # the sum of len and 6(maximum wrong attemps possible) is the max range possible
    lst_hit = []
    print(underline_choice)
    print(f'tip: {tip_choice}')
    user_choice = input('Digite sua tentativa: ')

    if user_choice in word_choice:
        print(colors.green + 'Você acertou' + colors.reset)

        for keys, values in enumerate(word_choice):
            if values == user_choice:
                lst_hit.append(keys)
        for pos in lst_hit:
            underline_choice = replacer(underline_choice, user_choice, pos)
    if underline_choice == word_choice:
        print(f'You Win')
        break

    else:
        cont_error += 1
        print(f'You lost the {lst_fail[cont_error - 1]}')
        if cont_error >= 6:
            print('Você perdeu todas as chances!!')
            break
