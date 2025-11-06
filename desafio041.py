from datetime import date
atual = date.today().year
nascimento = int(input('Informe o ano de nascimento do atleta: '))
idade = atual - nascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFATIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
elif idade > 25:
    print('Classificação: MASTER')
else:
    print('Opção Inválida. Tente Novamente!')