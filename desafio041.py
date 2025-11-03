from datetime import date
atual = date.today().year
nascimento = int(input('Informe o ano de nascimento do atleta: '))
idade = atual - nascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('O atleta está na categoria MIRIM')
elif idade <= 14:
    print('O atleta está na categoria INFATIL')
elif idade <= 19:
    print('O atleta está na categoria JUNIOR')
elif idade <= 20:
    print('O atleta está na categoria SÊNIOR')
else:
    print('O atleta está na categoria MASTER')