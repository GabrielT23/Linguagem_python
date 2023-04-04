while True:
    num = int(input('Digite um número entre 0 e 20:'))
    if 0 <= num <= 20:
        break
extensos = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desesseis', 'desesete', 'desoito', 'desenove', 'vinte')
print(f'você digitou o número {extensos[num]}')
