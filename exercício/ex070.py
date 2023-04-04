Tvalor = 0
Tprodutos = 0
menor = 0
while True:
    print('-'*30)
    print('Lojão Marineide')
    print('-' * 30)
    produto = str(input("nome do produto: ")).strip()
    valor = int(input("valor: R$"))
    Tvalor += valor
    if valor > 1000:
        Tprodutos += 1
    if menor == 0:
        menor = valor
    if valor < menor:
        menor = valor
    op = str(input('Quer continuar? [s/n]')).strip().upper()
    if op == 'N':
        break
print(f'Total da compra foi R${Tvalor}')
print(f'Total de produtos custando mais de R$1000: {Tprodutos}')
print(f'o menor valor foi: {menor}')
