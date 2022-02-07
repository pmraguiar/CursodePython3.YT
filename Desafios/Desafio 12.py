# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
#
print('Vamos fazer de tudo para te ajudar.')
v = float(input('Preciso que você me diga apenas quanto é o valor do produto: R$'))
# print('Pronto, com o nosso desconto o produto ficará por R$ {:.2f}.'.format(v-(5/100*v)))
print(f'Pronto, com o nosso desconto o produto ficará por R${v-(5/100*v):.2f}')
