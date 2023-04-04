import random
s1 = input('primeiro aluno:')
s2 = input('segundo aluno')
s3 = input('terceiro aluno')
s4 = input('quarto aluno')
lista = (s1, s2, s3, s4)
escolhido = (random.choice(lista))
print(f'O aluno esolhido foi {escolhido}')


