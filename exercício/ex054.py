from datetime import date
maior = 0
menor = 0
atual = date.today().year
for c in range(1, 8):
    nas = int(input(f'Em que ano a {c}° nasceu?'))
    idade = atual - nas
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E também tivemos {menor} pessoas menores de idade')
