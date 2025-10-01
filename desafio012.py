#valor = float(input('Digite o valor do produto: R$'))
#desconto = valor * 0.05
#resultado = valor - desconto
#print('Valor do produto com 5% de desconto é {:.0f}'.format(resultado))

preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O produto que cusatava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(preço, novo))