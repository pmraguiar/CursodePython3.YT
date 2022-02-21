si = 0 # Soma de todas as idades.
mi = 0 # Média das idades.
mih = 0 # Maior idade dos homens.
nhmv = 0 # Nome do homem mais velho.
totmulher20 = 0 # Total de mulheres com menos de 20 anos.
for c in range(1, 5):
    print(f'------{c}º PESSOA------')
    nome = str(input('NOME: ')).strip().title()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    si += idade
    if c == 1 and sexo in 'Mm':
        mih = idade
        nhmv = nome
    if sexo in 'Mm' and idade > mih:
        mih = idade
        nhmv = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
media = si / 4
print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {mih} anos e se chama {nhmv}.')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')
