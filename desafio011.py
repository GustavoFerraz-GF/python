lm = float(input('Qual a largura da parede em metros? '))
am = float(input('Qual a altura da parede em metros? '))
s = lm * am
a = s / 2
print('A área total é {:.0f}m²'.format(s))
print('E a quantidade de tinta para pintar a área é de {:.0f} litros'.format(a))