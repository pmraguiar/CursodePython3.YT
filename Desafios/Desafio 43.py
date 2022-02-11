# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, conforme a
# tabela abaixo:
# — Abaixo de 18.5: Abaixo do peso
# — Entre 18.5 e 25: Peso ideal;
# — 25 até 30: Sobrepeso;
# — 30 até 40: Obesidade;
# — Acima de 40: Obesidade mórbida
# IMC = PESO / (ALTURA X ALTURA)
print('-_-_' * 9)
print('\033[34mSEJA BEM VINDO A CALCULADORA DE IMC!\033[m')
print('-_-_' * 9)
nome = str(input('Como você se chama? ')).title()
print(f'Que nome bonito, {nome}!')
peso = float(input('Vamos lá, qual o seu peso? (Kg) '))
altura = float(input('Ok, e qual a sua altura? (m) '))
imc = peso / pow(altura, 2)
if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f}kg/m², e você está abaixo do peso.')
elif 18.5 < imc < 25:
    print(f'Seu IMC é de {imc:.2f}kg/m² e você está com o peso ideal. Parabéns, continue assim!')
elif 25 <= imc < 30:
    print(f'Seu IMC é de {imc:.2f}kg/m² e você está com sobrepeso.')
elif 30 <= imc < 40:
    print(f'Seu IMC é de {imc:.2f}kg/m² e você está com obesidade. Cuidado.')
elif imc >= 40:
    print(f'Seu IMC é de {imc:.2f}kg/m² e você está com obesidade mórbida. Procure um médico especialista.')
