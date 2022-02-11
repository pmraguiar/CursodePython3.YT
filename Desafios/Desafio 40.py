# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# conforme a média atingida:
# — Média abaixo de 5.0: REPROVADO
# — Média entre 5.0 e 6.9: RECUPERAÇÃO
# — Média 7.0 ou superior: APROVADO
#
n1 = float(input('Qual foi sua primeira nota? '))
n2 = float(input('Qual foi sua segunda nota? '))
media = (n1 + n2) / 2
if media < 5.0:
    print(f'Infelizmente você está reprovado, pois teve uma média de {media:.1f}.')
elif 5.0 <= media <= 6.9:
    print(f'Você atingiu a média {media:.1f} e está de recuperação.')
else:
    print(f'Parabéns! Você atingiu a média {media:.1f} e está APROVADO.')
