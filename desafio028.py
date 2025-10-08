from random import randint
from time import sleep # Dá um tempo de espera
computador = randint(0, 5) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número pensei? ')) #Jogador tenta Adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabéns! Você coseguiu me vencer')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador, jogador))