print('\033[32m='*33)
print('\033[34mOs 10 TERMOS DE UMA PA')
print('\033[32m='*33)
a1 = int(input('\033[mPrimeiro termo:'))
r = int(input('Razão:'))
an = a1 + (10 - 1) * r
for c in range(a1, an, r):
    print(c, end=' > ')
print('Acabou')