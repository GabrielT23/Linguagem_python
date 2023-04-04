frase = str(input('Digite uma frase:')).strip()
print('a letra A aparece {} vezes na frase'.format(frase.upper().count('A')))
print('a primeira letra A apareceu na posição {}'.format(frase.upper().find('A')+1))
print('a ultima letra A apareceu na posição {}'.format(frase.upper().rfind('A')+1))



