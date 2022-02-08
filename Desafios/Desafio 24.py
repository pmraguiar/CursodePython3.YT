# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com "SANTO".
#
cidade = str(input('Diga o nome da cidade: ')).strip().title()
print(cidade[:5] == 'Santo')
