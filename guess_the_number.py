
import random
lst = list(range(1,10+1))
NumRandom = random.choice(lst)
Cont = 0
n1 = int(input('Digite seu palpite: '))
while n1 != NumRandom:
    n1 = int(input('Errou, digite seu palpite novamente: '))
    Cont += 1
print('Acertou')
print(f'O total de tentativa(s) foi: {Cont}')
