print('\033[33m-=-'*20)
print('\033[32mAnalisador de Triângulos')
print('\033[33m-=-\033[m'*20)
a = float(input('Primeiro seguimento:'))
b = float(input('Segundo Seguimento:'))
c = float(input('Terceiro Seguimento:'))
if a+b < c or a+c < b or b+c < a:
    print(f'Os seguimentos {a}, {b} e {c} não podem formar um triângulo')
else:
    print(f'Os seguimentos {a}, {b} e {c} podem formar um triângulo')
