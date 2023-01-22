vel = float(input('Qual a velocidade atual do carro? '))
if vel <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print("MULTADO! você excedeu o limite permitido que é de 80km/h")
    multa = (vel-80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
