# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo
# que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.
#
v = float(input('Velocidade em km/h: '))
if v > 80:
    m = (v - 80) * 7
    print(f'Você está acima do limite da via por isso foi multado em R$ {m:.2f}.')
print('Tenha um bom dia! Dirija com segurança.')
