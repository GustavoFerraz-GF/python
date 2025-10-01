dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pago = (dia * 60) + (km * 0.15)
print('Total a pagar: R${:.2f}'.format(pago))