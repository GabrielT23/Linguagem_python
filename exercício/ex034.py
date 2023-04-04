s = float(input('Qual é o salário do funcionário?R$'))
if s <= 1250:
    ns = s * 1.15
else:
    ns = s * 1.10
print(f'Quem ganhava {s} passa a ganhar R${ns:.2f}.')
