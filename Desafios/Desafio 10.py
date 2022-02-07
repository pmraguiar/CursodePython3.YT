# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# ($1 = R$ 3.27).
#
print('Seja bem vindo à conversão automática.')
v = float(input('Me diga quanto você deseja converter em dólar: '))
# print('Prontinho, R$ {:.2f} dará exatos $ {:.2f}'.format(v, v/3.27))
print(f'Prontinho, R$ {v:.2f} dará exatos $ {v/3.27:.2f}.')
