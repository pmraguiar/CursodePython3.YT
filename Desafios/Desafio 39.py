# Faça um programa que leia o ano de nascimento de um jovem e informe, conforme a sua idade:
# — Se ele ainda vai se alistar ao serviço militar;
# — Se é a hora de se alistar;
# — Se já passou o tempo do alistamento.
# OBS: Seu programa deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano = date.today().year
nome = str(input('Olá, qual o seu nome? ')).strip().title()
nasc = int(input(f'Olá, {nome}. Qual o ano em que você nasceu? '))
alistamento = ano - nasc
if alistamento < 18:
    print(f'{nome} você deverá se alistar daqui {18 - alistamento} anos.')
elif alistamento == 18:
    print(f'{nome} está na hora de se alistar, você já completou 18 anos!')
else:
    print(f'{nome} você deveria ter se alistado há {alistamento - 18} anos.')
