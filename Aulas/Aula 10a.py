''' nome = str(input('Qual é seu nome? ')).strip().title()
if nome == 'Gustavo':
    print('Que nome lindo!')
else:
    print('Seu nome é bem comum, rs!')
print(f'Bom dia, {nome}!') '''
#
n1 = float(input('Qual foi a nota da primeira etapa? '))
n2 = float(input('Qual foi a nota da segunda etapa? '))
m = (n1 + n2) / 2
# if m >= 7.5:
#    print(f'Parabéns, sua média foi {m} e você passou de ano.')
# else:
#    print(f'Infelizmente sua média foi {m} e você não passou de ano.')
print('Parabéns, você passou de ano' if m >= 7.50 else 'Infelizmente você não passou de ano')
