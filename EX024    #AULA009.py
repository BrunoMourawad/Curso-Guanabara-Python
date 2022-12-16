#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome santo
cid = str(input('Digite a cidade em que você nasceu: ')).strip()
print(cid[:4].upper() =='BELO')
EX025    #AULA009
Crie um programa que leia o nome de uma pessoa e diga se ela tem ‘SILVA’ no nome.
nome = str(input('Digite seu nome completo: ')).upper().strip().split()
if 'SILVA' in nome:
    print(f'Seu nome TEM SILVA!')
else:
    print(f'Seu nome NÃO tem SILVA!')
