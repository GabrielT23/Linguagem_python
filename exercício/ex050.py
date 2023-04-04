soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('digite um numero'))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Dos 6 valores que você digitou {cont} são pares e a soma desses numeros é {soma}')



