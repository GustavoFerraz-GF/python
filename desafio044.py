preço = float(input('Valor do produto R$: '))

print(f'O valor do produto é R${preço:.2f}.')

print('''Formas de pagamentos:
      [1] Dinheiro ou cheque (10% de desconto)
      [2] Cartão à vista (5% de desconto)
      [3] Cartão em até 2x (sem juros)
      [4] Cartão 3x ou mais (20% de acréscimo)
''')

opção = int(input('Escolha a opção de pagamento: '))

cartão = preço - (preço * 5 / 100)
cartão3x = preço + (preço * 20 / 100)
if opção == 1:
    total = preço - (preço * 10 / 100)
    print(f'Pagando à vista no dinheiro/cheque, o produto sai por R${total:.2f}.')
elif opção == 2:
    total = preço - (preço * 5 / 100)
    print(f'Pagando à vista no cartão, o produto sai por R${total:.2f}.')
elif opção == 3:
    total = preço
    print(f'parcelando em até 2x no cartão, o produto mantém o valor de R${total:.2f}.')
elif opção == 4:
    total = preço + (preço * 20 / 100)
    print(f'Parcelando em 3x ou mais, o produto sai por R${total:.2f}')
else:
    print('Opção inválida! Tente novamente')