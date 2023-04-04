from datetime import date
nasc = int(input('Ano de nascimento:'))
idade = date.today().year - nasc
print(f'tem O atleta tem {idade}')
if idade <= 9:
    print('Categoria: Mirim')
elif idade > 9 and idade <= 14:
    print('Categoria: Infanti')
elif idade > 14 and idade <= 19:
    print('Categoria: Junior')
elif idade > 19 and idade <= 25:
    print('Categoria: Senior')
else:
    print('Categoria: Master')







