s = str(input('Digite seu sexo: [M/F]:')).upper()[0].strip()
while s not in 'MmFf':
    s = str(input('Dados invalidos. por favor digite novamente:')).upper()[0].strip()
print(f'Sexo {s} registrado com sucesso')
