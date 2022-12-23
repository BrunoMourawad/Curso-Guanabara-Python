#Crie um programa que faça o computador jogar jokenpô com você.

from random import randint
itens = ('Pedra','Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('==' * 13)
print('O computador jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print('==' * 13)
if computador == 0:
    if jogador == 0:
        print('Deu empate!!! Nem eu nem tu🤣 ')
    elif jogador == 1:
        print('Você ganhou, pensei que os humanos não fossem tão inteligentes🤷')
    elif jogador == 2:
        print('EU GANHEEEEI, HAHA HUMANOS E SUAS LIMITAÇÕES😎🤏')

elif computador == 1:
    if jogador == 1:
        print('Deu empate!!! Como eu pude empatar com um HUMANO? 🤦️')
    elif jogador == 2:
        print('Você ganhou, mas saiba que eu deixei🤷️')
    elif jogador == 0:
        print('EU GANHEEEEI, OS HUMANOS SÃO RUINS EM TUDO?🤷️')
    
elif computador == 2:
    if jogador == 2:
        print('Deu empate!!! Pode comemorar👏🎉 ')
    elif jogador == 0:
        print('Você ganhou, você não é mais um completo fracassado👍')
    elif jogador == 1:
        print('MUITO FÁCIL GANHAR DE HUMANOS😂😂😂😂🤏')


