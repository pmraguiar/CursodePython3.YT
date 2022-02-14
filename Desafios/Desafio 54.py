from datetime import date
atual = date.today().year # Importei o ano atual
contador = 0 # Comecei o contador de quem atingiu 21 anos
na = 0 # Comecei o contador de que não atingiu 21 anos
for i in range(1, 8):
    ano = int(input('Qual seu ano de nascimento? ')) # Ler o ano de nascimento de 7 pessoas
    if atual - ano >= 21: # Separei quem já atingiu 21 anos
        contador += 1 # Fiz a contagem
    elif atual - ano < 21: # Separei que não atingiu 21 anos
        na += 1 # Fiz a contagem
print(f'{contador} pessoas atingiram a maior idade e {na} não atingiram.')
