v = float(input('\033[1;32mqual a velocidade do carro?'))
if v >= 80:
    m = (v-80)*7
    print('\033[31mmultado! você excedeu o limite permitido que é 80km/h')
    print(f'você deve pagar uma multa de \033[33mR${m:.2f}!')
print('\033[34mtenha um bom dia e dirija com segurança')
