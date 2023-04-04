d = float(input('Qual é a dstância da viagem?'))
print(f'Você está prestes a começar uma viagem de {d}')
if d <= 200:
    p = d * 0.5
else:
    p = d * 0.45
print(f'o preço da sua passagem é R${p:.2f}')
