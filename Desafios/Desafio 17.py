# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retânngulo, calcule
# e mostre o comprimento da hipotenusa.
#
from math import hypot
co = float(input('Me diga o comprimento do cateto oposto: '))
ca = float(input('Me diga o comprimento do cateto adjacente: '))
h = hypot(co, ca)
print(f'O valor da hipotenusa será de {h:.2f}.')
