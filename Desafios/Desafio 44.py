# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento:
# — À vista dinheiro/PIX: 10% de desconto;
# — À vista no cartão: 5% de desconto;
# — Em até 2x no cartão: Preço normal;
# — 3x ou mais no cartão: 20% de juros.
#
print(f'{" Lojas Meireles ":=^40}')
normal = float(input('Qual o valor do produto? R$'))
print('''Escolha o modo de pagamento:
[ 1 ] À vista dinheiro ou PIX: 10% de desconto
[ 2 ] À vista no cartão: 5% de desconto
[ 3 ] Em até 2x no cartão: Preço normal
[ 4 ] 3x ou mais no cartão: 20% de juros''')
opcao = int(input('Sua opção: '))
pix = normal - (normal * 10 / 100)
cartao = normal - (normal * 5 / 100)
parcelado = normal + (normal * 20 / 100)
if opcao == 1:
    print(f'O valor a ser pago, será de R${pix:.2f}')
elif opcao == 2:
    print(f'O valor a ser pago será de R${cartao:.2f}')
elif opcao == 3:
    print(f'O valor a ser pago será de R${normal:.2f}')
elif opcao == 4:
    parcelas = int(input('Em quantas parcelas? '))
    parcela = parcelado / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R${parcela:.2f}'
          f'\nO valor total será de R${parcelado:.2f}')
else:
    print('\033[31mOpção incorreta.\033[m')

