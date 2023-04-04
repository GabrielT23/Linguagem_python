print('\033[32m='*33)
print('\033[34mOs 10 TERMOS DE UMA PA')
print('\033[32m='*33)
a1 = int(input('\033[mPrimeiro termo:'))
r = int(input('Razão:'))
termo = a1
cont = 1
while cont <= 10:
    print(f'{termo} > ', end='')
    termo += r
    cont += 1
print('FIM')