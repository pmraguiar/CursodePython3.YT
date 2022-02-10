n = str(input('Qual o seu nome? ')).strip().title()
if n == 'PEDRO':
    print('Que nome bonito.')
elif n == 'Gustavo' or n == 'Paulo' or n == 'Maria':
    print('É um nome legal e popular no Brasil.')
elif n in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino.')
# else:
#    print('É um nome bonito, porém comum.')
print(f'Tenha um bom dia, {n.title()}!')
