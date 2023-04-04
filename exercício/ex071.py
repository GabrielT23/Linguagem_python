print('-'*30)
print('POWER GUIDO')
print('-' * 30)
valor = int(input("valor: R$"))
cd100 = valor//100
valor = valor - cd100*100
cd50 = valor // 50
valor = valor - cd50 * 50
cd20 = valor // 20
valor = valor - cd20 * 20
cd10 = valor // 10
valor = valor - cd10 * 10
cd5 = valor // 5
valor = valor - cd5 * 5
cd2 = valor // 2
valor = valor - cd2 * 2
print(f'{cd100} cedulas de R$100')
print(f'{cd50} cedulas de R$50')
print(f'{cd20} cedulas de R$20')
print(f'{cd10} cedulas de R$10')
print(f'{cd5} cedulas de R$5')
print(f'{cd2} cedulas de R$5')