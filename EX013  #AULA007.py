#Faça um algoritmo que leia o salário de um funcionário  e mostre seu novo salário com 15% de aumento
sal = float(input('Qual o salário do funcionário? R$'))
aum = sal+(sal*15/100)
print ('Um funcionário que ganhava R${}, com 15% de aumento vai passar a receber R${}'.format(sal, aum))
