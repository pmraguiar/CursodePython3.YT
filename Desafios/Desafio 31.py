# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50
# por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.
#
d = float(input('Qual a distância da viagem em km: '))
if d <= 200:
    vc = d * 0.50
else:
    vc = d * 0.45
print(f'O valor da viagem será de R${vc:.2f}.')
