print('Seja bem vindo ao seu somador automático!!')
nome = input('Primeiro, gostaria de saber seu nome:')
print('Olá,{}! vamos começar!'.format(nome))
n1 = int(input('Me diga o primeiro número que iremos somar:'))
n2 = int(input('Agora me diga seu segundo número:'))
print('Muito obrigado, só um instante enquanto eu faço a soma..')
print('...')
z = n1 + n2
# print('Prontinho, a soma entre', n1, 'e', n2, 'é igual à {}!'.format(z))
# print('Prontinho, a soma entre {} e {} vale {}'.format(n1,n2,z))
print(f'Prontinho, a soma entre {n1} e {n2} é {z}')

