c = soma = cont = 0
while c != 999:
    c = int(input('Digite um numero [999 pra parar]:'))
    if c != 999:
        soma += c
        cont += 1
print(f'Você digitou {cont} numeros e a soma entre eles foi {soma}')

