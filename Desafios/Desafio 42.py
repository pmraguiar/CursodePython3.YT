# Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# — Equilátero: Todos os lados iguais;
# — Isósceles: Dois lados iguais;
# — Escaleno: Todos os lados diferentes.
#
l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos FORMAM um triângulo.')
