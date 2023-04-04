nome = str(input('Digite seu completo ')).strip()
print('Analisando seu nome... ')
print(f'seu nome em maiusculas é {nome.upper()}')
print(f'seu nome em minusculas é {nome.lower()}')
print('seu nome tem ao todo {} letras'.format(len(nome)- nome.count(' ')))
print(f'seu nome primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras')




