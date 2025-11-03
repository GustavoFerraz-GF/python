peso = float(input('Qual o seu peso (kg)? '))
altura = float(input('Qual a sua altura (m)? '))
total = peso / (altura ** 2)
print(f'Seu peso é {peso:.1f} Kg, sua altura é {altura:.2f} m.')
print(f'Seu IMC é {total:.2f}.')
if total <= 18.5:
    print('Abaixo do peso.')
elif total <= 25:
    print('Peso ideal.')
elif total <= 30:
    print('Sobrepeso.')
elif total <= 40:
    print('Obesidade.')
else:
    print('Obesidade Mórbida.')
