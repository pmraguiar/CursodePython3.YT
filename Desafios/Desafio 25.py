# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
#
nome = str(input('Nome completo: ')).strip().title()
print('Silva' in nome.split())
