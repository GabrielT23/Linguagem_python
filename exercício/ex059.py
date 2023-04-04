n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
o = 0
while not o == 5:
    print('''    [1] soma
    [2] multiplicar
    [3] maior
    [4] novos valores
    [5] sair do programa''')
    o = int(input('>>>>>> Qual a sua opção?'))
    if o == 1:
        print(f'A soma entre {n1} + {n2} é {n1+n2}')
    elif o == 2:
        print(f'A multiplicação de {n1} x {n2} é {n1*n2}')
    elif o == 3:
        if n1 > n2:
            maior = n1
        elif n1 < n2:
            maior = n2
        else:
            maior = 'não há maior'
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif o == 4:
        print(('Informe os numeros novamente:'))
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    elif o > 5:
        print('Opção inválida. Tente novamente')
    print('=-=='*10)
print('Fim do programa. Volte sempre!')
