nome = input('Digite seu nome completo: ')
print(nome.upper())
print(nome.lower())
tamanho1 = len(''.join(nome.split()))
print(tamanho1)
primeiro_nome = nome.split()[0]
tamanho2 = len(primeiro_nome)
print(tamanho2)