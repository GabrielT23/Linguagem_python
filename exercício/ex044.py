print('{:=^40}'.format('Loja tome no seu cu'))
c = float(input('Preço das compras:'))
print('FORMAS DE PAGAMENTO')
print('[1] à vista dinheiro/cheque')
print('[2] à vista cartão')
print('[3] 2x no cartão')
print('[4] 3x no cartão')
p = int(input('Qual a opção?'))
if p == 1:
    v = c * 0.9
    print(f'Sua compra de R${c} vai custar R${v} no final')
elif p == 2:
    v = c * 0.95
    print(f'Sua compra de R${c} vai custar R${v} no final')
elif p == 3:
    v = c
    print(f'Sua compra será parcelada em 2x de {c/2} sem juros')
    print(f'Sua compra vai custar R${v} no final ')
elif p == 4:
    v = c * 1.2
    q = int(input('Quantas parcelas?'))
    print(f'sua compra será parcelada em {q}x de {v/q} com juros')
    print(f'Sua compra de R${c} vai custar R${v} no final ')
