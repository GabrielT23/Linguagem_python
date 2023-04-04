from datetime import date
an = int(input('Ano de nascimento:'))
idade = 2021-an
atual = date.today().year
if idade < 18:
    print(f'Quem nasceu em {an} tem {idade} anos em {atual}. Ainda faltam {18-idade} para o alistamento.\nseu alistamento será em {atual+(18-idade)}')
elif idade == 18:
    print(f'Quem nasceu em {an} tem {idade} anos em {atual}.\nvocê tem que se alistar imediatamente!')
else:
    print(f'quem nasceu em {an} tem {idade} anos em {atual}. você já deveria ter se alistado há {idade-18} anos.\nSeu alistamento foi em {atual-(idade-18)}')


