# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo
# o nome deles e escrevendo o nome do escolhido.
#
from random import choice
n1 = str(input('Diga o nome do primeiro aluno: '))
n2 = str(input('Diga o nome do segundo aluno: '))
n3 = str(input('Diga o nome do terceiro aluno: '))
n4 = str(input('Diga o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
e = choice(lista)
print(f'O aluno escolhido foi o(a) {e}.')
