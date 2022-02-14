num = int(input('Digite um número inteiro: '))
if num % 1 == 0 and num % num == 0:
    print('O número digitado é primo.')
else:
    print('O número não é primo.')
