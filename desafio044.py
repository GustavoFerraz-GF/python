print('LOJAS FERRAZ')
preço = float(input('Preço das Compras: R$ '))

print(f'O valor do produto é R${preço:.2f}.')

print('''Formas de pagamentos:
      [1] Dinheiro ou cheque (10% de desconto)
      [2] Cartão à vista (5% de desconto)
      [3] Cartão em até 2x (sem juros)
      [4] Cartão 3x ou mais (20% de acréscimo)
''')
opção = int(input('Qual a opção de pagamento? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcelas = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcelas:.2f}.')
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparcelas = int(input('Quantas parcelas? '))
    parcelas = total / totalparcelas
    print(f'Sua compra será parcelada em {totalparcelas}x de R${parcelas:.2f} COM JUROS.')
else:
    total = 0
    print('Opção inválida de Pagamento! Tente novamente')
print(f'Sua compra de R$ {preço:.2f} vai custar R${total:.2f} no final.')
