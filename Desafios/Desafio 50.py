soma = 0
for c in range(1, 7):
    num = int(input('Digite um número: ')) # Ler 6 números
    if num % 2 == 0: # Pegará apenas os pares
        soma += c # Acumulador/Soma dos valores pares.
print(soma)
