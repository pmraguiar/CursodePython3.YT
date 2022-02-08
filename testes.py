from random import sample
n1 = str(input('nome 1: '))
n2 = str(input('nome 2: '))
n3 = str(input('nome 3: '))
escolhido = sample([n1, n2, n3], k=2)
print(escolhido)
