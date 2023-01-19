#Refaça o exercício o desafio 009, mostrando a tabuada de um número que o usuário escolheu, só que agora utilizando o laço for.
num = int(input('Digite um número para ver a sua tabuada: '))
for c in range (1,11):
    print('{} X {:2} = {}'.format(num, c, num*c))
