soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma = soma + c
print(f'O valor da soma de todos os {cont} valores solicitados é {soma}')
