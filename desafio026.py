frase = input('Digite uma frase: ').lower()
primeiro = frase.find('a') + 1
ultimo = frase.rfind('a') + 1
print(frase.count('a', 0))
print('{}'.format(primeiro))
print('{}'.format(ultimo))