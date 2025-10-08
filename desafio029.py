velocidade = int(input('Qual a velocidade atual do carro? '))
limite = 80
multa_por_km = 7
km_acima = velocidade - limite
pagar = km_acima * multa_por_km
if velocidade > limite:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print('Você deve pagar uma multa de R$ {:.2f}'.format(pagar))
   
print('Tenha um bom dia! Dirija com segurança!')