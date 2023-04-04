pesos = []
for a in range(1, 6):
    peso = float(input("digite seu peso: "))
    pesos.append(peso)
print(pesos)
print('maior peso é {}kg'.format(max(pesos)))
print('menor peso é {}kg'.format(min(pesos)))