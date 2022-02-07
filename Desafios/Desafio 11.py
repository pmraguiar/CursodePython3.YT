# Faça um programa que leia a LARGURA e a ALTURA de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m^2.
#
print('Bem vindo. Vou precisar apenas de alguns dados.')
afi = input('Certinho??')
larg = float(input('Que ótimo! Me diga primeiramente a largura (em metros): '))
h = float(input('Show, agora me diga a altura (em metros): '))
a = larg * h
# print('Pronto, a sua área é de {}. Para isso você precisará de {:.2f} litros de tinta.'.format(a, a/2))
print(f'Pronto, a sua área é de {a:.2f}m. Para isso você precisará de {a/2:.1f}L de tinta.')
