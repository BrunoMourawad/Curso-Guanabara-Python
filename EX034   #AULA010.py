#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00 calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%
sal = float(input('Qual o seu salário atual: '))
if sal > 1250.0:
    print('Parabéns, você recebeu um aumento de 10%, o seu salário atual é {:.2f}'.format(sal/10+sal))
else:
    print('Parabéns, você recebeu um aumento de 15%, o seu salário atual é {:.2f}'.format(sal/15+sal))
