nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print(f'Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {média:.1f}')
if média < 5:
    print('O aluno está REPROVADO.')
elif 7 > média >= 5:
    print('O aluno está de RECUPERAÇÃO')
elif média >= 7:
    print('O aluno está APROVADO')
else:
    print('Opção inválida! Tente novamente.')