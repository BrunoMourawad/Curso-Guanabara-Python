#Faça um programa que leia um ano de nascimento de um jovem e informe, de acordo com a sua idade. –Se ele ainda vai se alistar ao serviço militar. – Se é a hora de se alistar. –Se já passou do tempo de se alistar.
O seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
(verificar como aplica-se o plural na condições. Ex: ano e anos)

id = int(input('Digite a sua idade: '))
if id<18:
    print('Faltam {} anos para você completar 18 anos, assim que completar 18 anos procure a junta militar da sua cidade:'.format((id-18)*-1))
elif id>18:
    print('Você está {} anos atrasado para se alistar, procure uma junta militar imediatamente. '.format(id-18))
else:
    print('Você atualmente tem 18 anos, procure a junta militar mais próxima')
# #######Solução do guanabara
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
     print('Você tem que se alistar imediatamente')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos, faltam {} anos para o alistamento'.format(saldo))
    print('Seu alistamento será em {}'.format(ano))
    ano = atual + saldo
elif idade > 18:
    saldo = idade - 18
    print('Você ja deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print ('Seu alistamento foi em {}'.format(ano))

#####Solução do guanabara abaixo
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
     print('Você tem que se alistar imediatamente')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos, faltam {} anos para o alistamento'.format(saldo))
    print('Seu alistamento será em {}'.format(ano))
    ano = atual + saldo
elif idade > 18:
    saldo = idade - 18
    print('Você ja deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print ('Seu alistamento foi em {}'.format(ano))



