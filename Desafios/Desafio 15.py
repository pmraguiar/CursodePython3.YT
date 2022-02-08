# Escreva um programa que perunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 6o,00 por dia e R$ 0,15 por km rodado
dias = int(input('Quantos dias foram alugados? '))
km = float(input('Quantos km foram rodados: '))
# pd = dias * 60
# pkm = km * 0.15
# vt = pd + pkm
# print('O total a pagar é de R${}.'.format(vt))
print(f'O total a pagar será de R$ {(dias*60)+(km*0.15):.2f}')
