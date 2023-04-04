soma = 0
maioridade = 0
nomevelho = ''
mulheres = 0
media = 0
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = str(input('Sexo[M/F]:').upper())
    soma += idade
    media = soma/c
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if c == 1 and sexo == 'M':
        maioridade = idade
        nomevelho = nome
    elif c != 1 and sexo == 'M':
        if idade > maioridade:
            maioridade = idade
            nomevelho = nome
print(f'A media da idade do grupo é de {media} anos')
print(f'O homem mais velho tem {maioridade} e se chama {nomevelho}')
print(f'Ao todo são {mulheres} com menos de de 20 anos')








