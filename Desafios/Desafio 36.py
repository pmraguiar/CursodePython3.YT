# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar
# o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai PAGAR. Calcule o valor da prestação mensal,
# sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
#
from time import sleep
print('\033[97m=-=\033[m' * 19)
print('\033[36mBem vindo ao simulador de empréstimo do Banco do Gatinho\033[m')
print('\033[97m=-=\033[m' * 19)
nome = str(input('Qual o seu nome? ')).strip().title()
casa = float(input('Qual o valor da casa que está querendo comprar? R$'))
sal = float(input('Qual seu salário? R$'))
tempo = int(input('Quantos anos você quer financiar? '))
print(f'OK, {nome}, estamos analisando...')
sleep(2)
meses = tempo * 12
parcela = casa / meses
condicao = sal * 30 / 100
if condicao >= parcela:
    print(f'\033[35mParabéns\033[m, {nome}, \033[35mvocê conseguiu\033[m o empréstimo para a compra da sua casa. '
          f'Você irá pagar R${parcela:.2f} durante {meses} meses.')
else:
    print(f'{nome}, \033[33minfelizmente\033[m, seu empréstimo foi negado. A prestação será de R${parcela:.2f}.')
