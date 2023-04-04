Tmaior = 0
Thomens = 0
tmulher = 0
while True:
    print('CADASTRE UMA PESSOA')
    idade = int(input("Idade: "))
    sexo = str(input("Sexo:[M/F] ")).strip().upper()
    while sexo not in 'MnFf':
        sexo = str(input("Sexo:[M/F] ")).strip().upper()
    if idade > 18:
        Tmaior += 1
    if sexo == 'M':
        Thomens += 1
    else:
        if idade < 20:
            tmulher += 1
    op = str(input('Quer continuar? [s/n]')).strip().upper()
    if op == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {Tmaior}')
print(f'Total de homens cadastrados: {Thomens}')
print(f'Total de mulheres com menos de 20 anos: {tmulher}')