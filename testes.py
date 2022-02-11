from random import randint
from time import sleep
pc = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 8)
print(f'O computador jogou {pc}')
print(f'O jogador jogou {jogador}')
print('-=' * 8)