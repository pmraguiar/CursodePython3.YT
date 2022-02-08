# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#
num = int(input('Número de 0 a 9999: '))
# n = str(numero)
# print(f'Analisando o número {numero}:')
# print(f'Unidade: {n[3]}')
# print(f'Dezena: {n[2]}')
# print(f'Centena: {n[1]}')
# print(f'Milhar: {n[0]}')
print(f'Unidade: {num // 1 % 10}')
print(f'Dezena: {num // 10 % 10}')
print(f'Centena: {num // 100 % 10}')
print(f'Milhar: {num // 1000 % 10}')
