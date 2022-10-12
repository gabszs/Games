import random

jokenpo = ["PEDRA", "PAPEL", "TESOURA"]
pc_choice = random.choice(jokenpo)

print(pc_choice)
user_attempt = input('Digite em letra maiuscula a sua tentativa: ')
if user_attempt != pc_choice:
    if (user_attempt == 'TESOURA' and pc_choice == 'PAPEL') \
            or (user_attempt == 'PAPEL' and pc_choice == 'PEDRA') \
            or (user_attempt == 'PEDRA' and pc_choice == 'TESOURA'):
        print('Você Venceu')
    else:
        print('Você Perdeu')
else:
    print('Deu empate')
