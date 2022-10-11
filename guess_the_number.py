import random

# guess the number game
lst_numbers = [num for num in range(0,11)]  # uses a list comprehesion to create a list from 0 to 10
num_random = random.choice(lst_numbers)
cont_error = 0

user_try = int(input('Try a number from 0 to 10: '))  # declare int with input as the user attempt

while user_try != num_random:  # a while loop to give another opportunies to the user to guess the number
    user_try = int(input('Wrong, try again: '))
    cont_error += 1

print('Nice try!!')
print(f'Congrats, you win, the total numbers of wrong attempts was: {cont_error}')
