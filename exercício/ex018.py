import math
an = float(input('digite o angulo que você deseja'))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tag = math.tan(math.radians(an))
print(f'o ângulo de {an} tem o seno de {sen:.2f}\no ângulo de {an} tem o cosseno de {cos:.2f}\no ângulo de {an} tem a tangente de {tag:.2f}')

