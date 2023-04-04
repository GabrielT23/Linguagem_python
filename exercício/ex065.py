cmd = 'Ss'
soma = cont = maior = menor = 0
while cmd in 'Ss':
    n = int(input('Digite um número:'))
    soma += n
    cont += 1
    cmd = str(input('Quer continuar? [S/N] ')).upper()[0].strip()
    if cont == 1:
        maior = menor = n
    if n < menor:
        menor = n
    if n > maior:
        maior = n
print(f'''Você digitou {cont} números e a média foi {soma/cont}
O maior valor foi {maior} e o menor foi {menor}''')

