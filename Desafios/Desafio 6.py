# Crie um algoritmo que leia seu número e mostre o seu dobro, triplo e raíz quadrada.
#
n = int(input('Me diga um número:'))
print('O dobro será {}; \nO triplo {}; \nA raiz quadrada será {:.2f}.'.format(n*2, n*3, pow(n, (1/2))))
