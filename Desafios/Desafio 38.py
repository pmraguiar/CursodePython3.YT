# Escreva um programa que leia dois números inteiros e compare-os, mostrando uma mensagem na tela:
# — O primeiro valor é maior;
# — O segundo valo é maior;
# — Não existe valor maior, os dois são iguais.
#
n1 = int(input('Diga um número: '))
n2 = int(input('Diga outro número: '))
if n1 > n2:
    print(f'O {n1} é maior que {n2}.')
elif n2  > n1:
    print(f'O {n2} é maior que o {n1}.')
else:
    print('Não existe número maior, os dois são iguais.')
