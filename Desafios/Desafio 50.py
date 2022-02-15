soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite {c}° número: ')) # Ler 6 números
    if num % 2 == 0: # Pegará apenas os pares
        soma += num # Acumulador/Soma dos valores pares.
        cont += 1
print(f'Você informou {cont} números pares e a soma deles foi de {soma}.')
