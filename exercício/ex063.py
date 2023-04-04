print('\033[32m='*33)
print('\033[34mOs SEQUENCIA DE FIBONACCI')
print('\033[32m='*33)
cont = 3
q = int(input('\033[mQuantos termos você quer mostrar?'))
t1 = 0
t2 = 1
t3 = t2 + t1
print(f'{t1} > {t2} > {t3}', end=' > ')
while cont != q:
    t1 = t2
    t2 = t3
    t3 = t2 + t1
    print(t3, end=' > ')
    cont += 1
print('FIM')