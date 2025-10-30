casa = float(input('Valor da casa? '))
salário = float(input('Salário do comprador? '))
anos = int(input('Quantos anos de financiamento? ' ))
prestação = casa / (anos * 12)
mínimo = salário * 0.3
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${prestação:.2f}')
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')