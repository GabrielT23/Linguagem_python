peso = float(input('Digite o seu peso em kg?'))
altura = float(input('Digite a sua altura em metros?'))
imc = peso/(altura**2)
print(f'O imc dessa pessoa é {imc}')
if imc < 18.5:
    print('Você está abaixo do pessoa ideal')
elif 18.5 <= imc < 25:
    print('Parabéns! você está no peso ideal')
elif 25 <= imc < 30:
    print('Você está com sobrepeso')
elif 30 <= imc <40:
    print('Cuidado, você está obeso')
else:
    print('Nossa! você está com obesidade morbida')
