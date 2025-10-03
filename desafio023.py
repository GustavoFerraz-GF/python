numero = str(input('Informe um número: ')) 

unidade = len(numero[:4])
print('unidade: {}'.format(unidade))

dezena = len(numero[:3])
print('dezena: {}'.format(dezena))

centena = len(numero[:2])
print('centena: {}'.format(centena))

milhar = len(numero[:1])
print('milhar: {}'.format(milhar))