distancia = float(input('Qual a distância da sua viagem? '))
print(f'Você está preste a começar uma viagem de {distancia}Km')
limite = 200
valor_km_ate_limite = 0.50
valor_km_acima_limite = 0.45
if distancia <= limite:
    pagar = distancia * valor_km_ate_limite
else:
    pagar = distancia * valor_km_acima_limite
print(f'E o preço da sua passagem será de R${pagar:.2f}')


'''distancia = float(input('Qual é a distância da sua viagem? '))
print(f'Você está preste a começar uma viagem de {}km.')
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print(f'E o preço da sua passagem será R${preço:.2f}')'''


'''distancia = float(input('Qual é a distância da sua viagem? '))
print(f'Você está preste a começar uma viagem de {distancia}km.')
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'E o preço da sua passagem será R${preço:.2f}')'''