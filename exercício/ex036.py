vc = float(input('Qual o valor da casa?R$'))
vs = float(input('Qual o seu salário?R$'))
va = int(input('Em quantos anos você vai pagar essa casa?'))
p = vc/(va*12)
print(f'para comprar uma casa no valor de {vc} em {va} anos a prestação mensal será de {p:.2f}')
if p <= vs *0.30:
    print('\033[32mEmpréstimo aprovado')
else:
    print('\033[31mDesculpe, infelizmente você não poderá financiar essa casa')
