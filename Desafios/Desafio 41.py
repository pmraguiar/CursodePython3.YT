# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, conforme a idade:
# — Até 9 anos: MIRIM;
# — Até 14 anos: INFANTIL;
# — Até 19 anos: JUNIOR;
# — Até 20 anos: SÊNIOR;
# — Acima: MASTER.
#
from datetime import date
ano = date.today().year
nasc = int(input('Qual o ano do seu nascimento? '))
idade = ano - nasc
if idade <= 9:
    print(f'Você tem {idade} anos e faz parte da categoria MIRIM.')
elif 9 < idade <= 14:
    print(f'Você tem {idade} anos e faz parte da categoria INFANTIL.')
elif 14 < idade <= 19:
    print(f'Você tem {idade} anos e faz parte da categoria JUNIOR.')
elif 19 < idade <= 20:
    print(f'Você tem {idade} anos e faz parte da categoria SÊNIOR.')
else:
    print(f'Você tem {idade} anos e faz parte da categoria MASTER.')
print('Seja bem vindo a Confederação Nacional de Natação!')
