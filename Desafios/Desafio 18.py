# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do SENO, COSSENO e TANGENTE desse ângulo.
#
from math import sin, cos, tan, radians
a = float(input('Digite um ângulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print(f'O valor do seno é de {s:.2f}, do cosseno é de {c:.2f} e a tangente será {t:.2f}.')
