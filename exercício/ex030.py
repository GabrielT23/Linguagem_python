n = int(input('\033[35mMe diga diga um numero qualquer:'))
r = n % 2
if r == 1:
    print(f'\033[31mo numero {n} é impar')
else:
    print(f'o \033[32mnumero {n} é par')
