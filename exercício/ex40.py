n1 = float(input('Primeiro numero:'))
n2 = float(input('Segundo numero:'))
m = (n1+n2)/2
print(f'Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {m:.1f}')
if m <= 5:
    print('\033[31mO aluno está reprovado')
elif m >=7:
    print('\033[32mO aluno está aprovado')
else:
    print('\33[33mO aluno está de recuperação')
