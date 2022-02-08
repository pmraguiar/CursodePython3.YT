# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas OK
# - O nome com todas as letras minúsculas OK
# - Quantas letras ao td (sem considerar espaço)
# Quantas letras tem o primeiro nome
#
nome = str(input('Nome completo: ')).strip()
print(f'Seu nome com tudo maiúsculo: {nome.upper()}')
print(f'Seu nome com tudo minúsculo: {nome.lower()}')
nse = len(nome) - nome.count(' ')
print(f'Seu nome tem ao todo {nse} letras.')
# pn = nome.find(' ')
# print(f'Seu primeiro nome tem {pn} letras.')
separa = nome.split()
print(f'Seu primeiro é {separa[0]} e tem {len(separa[0])} letras.')
