from random import randint
print('-=' * 30)
print('Vamos jogar par ou impar')
print('-=' * 30)
while True:
    np = int(input('Digite um valor: '))
    while np > 10:
        np = int(input('você não tem mais que 10 dedos na mão. digite um valor menor ou igual a 10: '))
    op = str(input('par ou impar?[p/i]')).strip().upper()[0]
    nc = randint(0, 10)
    print(f'Você jogou {np} e o computador jogou {nc}. o total de deu {nc+np}')
    if op == 'P':
        if (np+nc)%2 != 0:
            print('você perdeu!')
        else:
            print('você venceu!')
            break
    if op == 'I':
        if (np+nc)%2 == 0:
            print('você perdeu')
        else:
            print('você venceu!')
            break
    print('-' * 30)
print('PROGRAMA PAR OU IMPAR. Volte sempre!')