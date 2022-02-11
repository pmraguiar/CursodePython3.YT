# Crie um programa que faça o computador jogar Jokenpô com você.
#
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('Vamos jogar JOKENPO??')
sleep(1)
print('''Escolha uma opção:
[ 0 ] \033[37mPEDRA\033[m
[ 1 ] PAPEL
[ 2 ] \033[35mTESOURA\033[m''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(0.6)
print('KEN')
sleep(0.6)
print('PO!!!')
sleep(0.6)
print('-=' * 14)
print(f'O computador jogou {itens[pc]}')
print(f'Você jogou {itens[jogador]}')
print('-=' * 14)
if jogador == pc:
    print('\033[33mEmpate!\033[m')
elif jogador == 0 and pc == 2 or jogador == 1 and pc == 0 or jogador == 2 and pc == 1:
    print('\033[33mVocê\033[m venceu!')
elif jogador == 2 and pc == 0 or jogador == 0 and pc == 1 or jogador == 1 and pc == 2:
    print('O \033[31mcomputador\033[m venceu!')
