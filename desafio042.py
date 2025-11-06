print('-='*20)
print('Analisando triângulos')
print('-='*20)
t1 = float(input('Primeiro segmento: '))
t2 = float(input('Segundo segmento: '))
t3 = float(input('Terceiro segmento: '))
if (t1 + t2 > t3) and (t1 + t3 > t2) and (t2 + t3 > t1):
    print(f'Os segmentos acima PODEM FORMAR um triângulo! ', end='')
    if t1 == t2 == t3:
        print('EQUILÁTERO')
    elif t1 != t2 != t3 != t1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print(f'Os segmentos acima NÃO PODEM FORMAR triângulo!')