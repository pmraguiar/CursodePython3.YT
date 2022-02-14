somador = 0
contador = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        contador = contador + 1 # Irá contar quantos achou, adicionando +1 a contagem. contador += 1
        somador = somador + c # Acumula os números achados. somador += c
print(f'A soma de todos os {contador} números será de {somador}.')
