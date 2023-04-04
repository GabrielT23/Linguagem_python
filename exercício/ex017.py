import math
b = float(input('comprimento do cateto oposto'))
c = float(input('comprimento do cateto adjacente'))
#a = math.sqrt(pow(b, 2) + pow(c, 2))
a = math.hypot(b, c)
print(f'o valor da hipotenusa é {a}')



