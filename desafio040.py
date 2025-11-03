nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print(f'A nota é {média}')
if média < 5:
    print('REPROVADO.')
elif média < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
