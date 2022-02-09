# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00 calcule um aumento de 10%. Para inferiores ou iguais, o aumento é de 15%.
#
n = str(input('Nome do funcionário: ')).title().strip()
s = float(input('Qual o salário do funcionário: '))
if s > 1250:
    sn = s + (s * 10 / 100)
else:
    sn = s + (s * 15 / 100)
print(f'O valor atualizado do salário do(a) {n} será de R${sn:.2f}.')
