frase = str(input('Digite uma frase:')).strip().upper()
separa = frase.split()
junto = ''.join(separa)
print(f'O inverso de {junto} é {junto[::-1]}')
if junto == junto[::-1]:
    print('A frase digitada é um palíndromo')
else:
    print('A frase digitada não é um palíndromo')





