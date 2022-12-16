#Escreva um programa que leia a velocidade de um carro, se ele ultrapassar a velocidade de 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada km acima do limite.
vl = int(input('Digite a velocidade do veículo: '))
if vl>80:
    multa = (vl-80)*7
    print('O seu veículo ultrapassou a velocidade permitida, valor da sua multa é {}'.format(multa))
else:
    print('O seu veículo estava dentro da velocidade permitida.')
