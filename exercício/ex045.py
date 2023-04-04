from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
c = randint(0, 2)
print('''Suas opções 
[0] pedra
[1] papel
[2] tesoura''')
j = int(input('Qual a sua jogada?'))
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po!!!')
print('-=-'*20)
print(f'jogador jogou {itens[j]}')
print(f'Computador jogou {itens[c]} ')
print('-=-'*20)
if c == j:
    print('empate')
elif c == 0 and j == 2 or c == 1 and j == 0 or c == 2 and j == 1:
    print('Computador ganhou')
elif j == 0 and c == 2 or j == 1 and c == 0 or j == 2 and c == 1:
    print('Jogador ganhou')
else:
    print('Jogada inválida')


