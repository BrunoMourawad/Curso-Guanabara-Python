#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
if  n % 2 == 0 or n % 5 == 0 or n % 3 == 0 or n % 7 == 0:
    if n != 2  or n != 5 or n !=7:
     print('O número {} NÃO é um número primo: '.format(n))
else:
     print ('O número {} é primo. '.format(n)) 



