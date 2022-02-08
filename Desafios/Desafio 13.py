# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
#
v = float(input('me diga quanto o funcionário recebe: R$'))
# print('Pronto, ele teve um aumento de 15%, então passará a ter um salário de: R$ {:.2f}'.format(v+(15/100*v)))
print(f'Pronto, ele teve um aumento de 15%, então passará a ter um salário de R${v+(15/100*v):.2f}.')
