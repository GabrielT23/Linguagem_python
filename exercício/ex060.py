n1 = int(input('Digite um numero para calcular o seu fatorial:'))
c = n1
fatorial = 1
while c > 0:
    print(f'{c}', end=' ')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1
print(fatorial)

