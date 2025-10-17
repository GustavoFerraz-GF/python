print('-='*20)
print('Analisando triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print(f'Os segmentos acima PODEM FORMAR triângulo!')
else:
    print(f'Os segmentos acima NÃO PODEM FORMAR triângulo!')