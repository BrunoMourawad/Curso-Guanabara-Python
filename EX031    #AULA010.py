#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens até 200km e 0,45 para viagens mais longas.
dis = int(input('Qual a distância em km da viagem? '))
if dis <= 200:
    print('Você viajou {:1} km, o valor da sua viagem é {:2} R$'.format(dis, (dis*0.50)))
else:
    print('Você viajou {:1} km, o valor da sua viagem é {:2} R$'.format(dis, (dis*0.45)))
