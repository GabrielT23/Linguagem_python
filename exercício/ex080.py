dicionario = dict()
dicionario['nome'] = str(input("Digite o nome do aluno:"))
dicionario['media'] = float(input("Digite a media do aluno:"))
if dicionario['media'] < 5:
    dicionario['situacao'] = 'reprovado'
else:
    dicionario['situacao'] = 'Aprovado'
print(dicionario)
