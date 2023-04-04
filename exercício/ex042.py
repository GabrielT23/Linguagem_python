print('\033[33m-=-'*20)
print('\033[32mAnalisador de Triângulos')
print('\033[33m-=-\033[m'*20)
a = float(input('Primeiro seguimento:'))
b = float(input('Segundo Seguimento:'))
c = float(input('Terceiro Seguimento:'))
if a < b + c and b < a + c and c < a + b:
    print(f'Os seguimentos {a}, {b} e {c} podem formar um triângulo', end='')
    if a == b ==c:
        print(' Equilatero!')
    elif a != b != c != a:
        print(' Escaleno!')
    else:
        print(' Isoceles!')
else:
    print(f'Os seguimentos {a}, {b} e {c} não podem formar um triângulo')
