frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() # Separar espaços e coloca em uma lista
junto = ''.join(palavras) # Irá juntar tudo, para desconsiderar espaços
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}.')
'''for letra in range(len(junto) - 1, -1, -1): # Fez o inverso dela. Foi da última letra até a primeira, voltando.
    inverso += junto[letra]'''
if inverso == junto:
    print('Temos um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')
