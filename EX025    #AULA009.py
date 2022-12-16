#Crie um programa que leia o nome de uma pessoa e diga se ela tem ‘SILVA’ no nome.
nome = str(input('Digite seu nome completo: ')).upper().strip().split()
if 'SILVA' in nome:
    print(f'Seu nome TEM SILVA!')
else:
    print(f'Seu nome NÃO tem SILVA!')
