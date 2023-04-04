maioridade = 0
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    idade = int(input('Idade:'))
    sexo = str(input('Sexo[M/F]:').upper())
    if c == 1 and sexo == 'M':
        maioridade = idade
    elif c != 1 and sexo == 'M':
        if idade > maioridade:
            maioridade = idade
print(maioridade)


