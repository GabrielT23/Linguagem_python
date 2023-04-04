cont = 0
n = int(input('Digite um numero:'))
for c in range(1, n+1):
    if n % c == 0:
        print(f'\033[33m{c}', end=' ')
        cont += 1
    if n % c != 0:
        print(f'\033[31m{c}', end=' ')
print(f'\n\033[mO número {n} foi divisível {cont} vezes')
if cont <= 2:
    print('\033[me por isso O numero é primo')
else:
    print('\033[me por isso o numero não é primo')
