# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
#
n = float(input('Me diga quantos metros você quer converter: '))
print('Prontinho, {} metros tem exatos \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'
      .format(n, (n/1000), (n/100), (n/10), (n*10), (n*100), (n*1000)))
