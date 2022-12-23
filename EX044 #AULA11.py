#Elabore um programa que calcule o valor a ser pago e a condição de pagamento:
-À vista dinheiro//cheque: 10% de desconto// À vista no cartão: 5% de desconto// Em 2x no cartão: preço normal// 3x ou mais 20% de juros

vl = float(input('Informe o valor do produto: '))
pag = int(input('\n(1) À vista dinheiro, pix ou cheque.\n(2) À vista crédito ou débito.\n(3) Em até 2x no cartão de crédito.\n(4) De 3x à 12x no cartão de crédito.\nDIGITE O NÚMERO CORRESPONDENTE À FORMA DE PAGAMENTO:'))
if pag == 1:
    print('Você ganhou 10% de deconto, o valor a ser pago é {}'.format(vl-(vl/100*10)))
elif pag == 2:
    print('Você ganhou 5% de desconto, o valor a ser pago é {}'.format(vl-(vl/100*5)))
elif pag == 3:
    print('O valor total é de {}, o pagamento deverá ser feito em duas parcelas de {}'.format(vl,(vl/2)))
elif pag == 4:
    tpc = int(input('Selecione de quantas vezes você deseja dividir. '))
    print ('O valor total é de {}, o pagamento será feito em {} vezes de {}'.format(vl/100*20+vl,tpc,(vl/100*20+vl)/tpc))

