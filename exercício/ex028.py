from random import randint
from time import sleep
n = randint(0, 5) # faz o computador pensar em um numero de 0 a 5
print('-=-'*100)
print('Vou pensar em numero entre 0 e 5. Tente adivinhar...')
print('-=-'*100)
e = int(input('em que numero eu pensei?')) # o jogador tenta adivinhar
print('processando...')
sleep(3)
if e == n:
    print('parabéns! você conseguiu me vencer!')
else:
    print(f'Ganhei! pensei no numero {n} e não no {e}')



