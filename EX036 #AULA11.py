##Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual o seu salário atual? '))
pag = int(input('Em quantos anos você vai pagar a casa? '))
pres = (casa/pag)/12
if pres>(sal/100)*30:
    print('O valor das prestações é maior que 30% do seu salário, empréstimo negado.')
else:
    print('Parabéns, o seu empréstimo foi aprovado! o valor das prestações é de {:.2f}'.format(pres))

