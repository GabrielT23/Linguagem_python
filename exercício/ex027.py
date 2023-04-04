nome = str(input('Digite seu nome completo:')).strip()
d = nome.split()
print('muito prazer em ti conhecer!')
print('seu primeiro nome é {}'.format(d[0]))
print('seu ultimo nome é {}'.format(d[len(d)-1]))


