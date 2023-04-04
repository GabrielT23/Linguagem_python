print('\033[32m='*33)
print('\033[34mOs 10 TERMOS DE UMA PA')
print('\033[32m='*33)
a1 = int(input('\033[mPrimeiro termo:'))
r = int(input('Razão:'))
termo = a1
op = 11
cont = 0
while op != 1:
    an = a1 + (op - 1) * r
    for c in range(a1, an, r):
        print(c, end=' > ')
        cont += 1
    print('Pausa')
    op = int(input('Quantos termos quer mostrar a mais?')) + 1
print(f'Foram mostrados ao todo {cont} termos.')