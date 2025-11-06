peso = float(input('Qual o seu peso (kg)? '))
altura = float(input('Qual a sua altura (m)? '))
imc = peso / (altura ** 2)
print(f'Seu peso é {peso:.1f} Kg, sua altura é {altura:.2f} m.')
print(f'Seu IMC é {imc:.1f}.')
if imc <= 18.5:
    print('Abaixo do peso.')
elif imc <= 25:
    print('Peso ideal.')
elif imc <= 30:
    print('Sobrepeso.')
elif imc <= 40:
    print('Obesidade.')
elif imc > 40:
    print('Obesidade Mórbida.')
else:
    print('Informação Incorreta. Tente Novamente!')
