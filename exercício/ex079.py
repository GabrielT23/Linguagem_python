cont = 0
lista = list()
while True:
    n = int(input("Digite um numero"))
    if n in lista:
        print("valor duplicado, não vou adicionar.")
    else:
        lista.append(n)
    op = str(input("Quer continuar?? [S/N]"))
    if op in 'nN':
        break
print(f'Os valores digitados foram: {lista}')