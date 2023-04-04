lista = list()
for c in range(0, 5):
    lista.append(int(input(f"Digite o {c+1}° valor")))
maior = max(lista)
menor = min(lista)
print(f"Os valores digitados foram: {lista}")
print(f"Dentre eles o maior foi {maior}")
print(f"Dentre eles o menor foi {menor}")
print(f'A posição de cada um deles é respectivamente {lista.index(maior)} e {lista.index(menor)}')
