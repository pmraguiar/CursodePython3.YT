# Escreva um programa que faça o pc "pensar" um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
# foi o número escolhido pelo computador.
#
from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
user = int(input('Qual número você acha que pensei? '))
computador = randint(0, 5)
print('Processando...')
sleep(2)
if user == computador:
    print('Parabéns, você acertou!!')
else:
    print(f'Infelizmente você errou. O computador escolheu o número {computador} e você o número {user}.')
