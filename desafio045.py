from random import randint
from time import sleep
computador = randint(0, 2)
print('''Vamos jogar JOKENPÔ? 
      [1] SIM
      [2] NÃO      
''')
opção = int(input('Escolha umas das opções acima: '))

if opção == 1:
    print('''Você terá que escolher um dos síbolos abaixo.
      [1] TESOURA
      [2] PAPEL
      [3] PEDRA
    ''')
    jogador = int(input('Escolha 1 entre os 3 símbolos: '))
    print('PROCESSANDO...')
    sleep(1)
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ')
    sleep(0.5)
    símbolos = {0:'Tesoura', 1:'Papel', 2:'Pedra'}
    print('-=' * 15)
    print(f'Você escolheu {símbolos[jogador]}')
    print(f'O computador escolheu {símbolos[computador]}')
    print('-=' * 15)
    if jogador == computador:
        print('EMPATE!')
    elif (jogador == 0 and computador == 1) or \
        (jogador == 1 and computador == 2) or \
        (jogador == 2 and computador == 0):
        print('VOCÊ GANHOU! 🎉')
    else:
        print('EU GANHEI! 😈')
elif opção == 2:
        print('Ok, quem sabe da próxima vez!')
        exit()
else:
    print('Opção inválida! TENTE NOVAMENTE.')