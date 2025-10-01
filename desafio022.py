nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')

print('Seu nome maiúsculas é: {}'.format(nome.upper()))

print('Seu nome minúsculas é: {}'.format(nome.lower()))

print('Seu mome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

#print('Seu nome tem ao todo {} letras'.format(nome.find(' ')))
#Gustavo

separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))