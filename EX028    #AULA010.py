#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
computador = randint (0, 5)
user = int(input('Adivinhe o número que o computador pensou: '))
if computador == user:
    print('Parabéns, você acertou o número ')
else:
    print ('Haha, você errou, pensei no número {}'.format(computador))
