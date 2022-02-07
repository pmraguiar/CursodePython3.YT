n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma vale {}!'.format(n1+n2))
print(f'A soma vale {n1+n2}!')
s = n1 + n2
m = n1 * n2
d = n1 / n2
e = n1 ** n2
di = n1 // n2
rd = n1 % n2
print('A soma é {}, \n a multiplicação é {} e a \n divisão é {:.3f}, a potência é {}'.format(s, m, d, e), end='. ')
print('Já a divisão inteira é {} e o restante é {}'.format(di, rd))
# o {:.3f} foi para dizer que queria apenas com 3 casas decimals. o f significa flutuantes.
# o end= foi para não haver duas linhas, ele irá juntar a linha de baixo com a de cima. \n -> indicar nova linha.
