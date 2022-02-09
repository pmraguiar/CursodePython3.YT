# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
#
n1 = float(input('Número 1: '))
n2 = float(input('Número 2: '))
n3 = float(input('Número 3: '))
lista = [n1, n2, n3]
print(f'O maior número é o {max(lista)} e o menor é o {min(lista)}.')
