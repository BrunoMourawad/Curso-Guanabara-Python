##Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: -1 para binário -2 para octal -3 para hexadecimal

n = int(input('Digite um número inteiro positivo: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para binário é igual a {}'.format(n, bin(n)[2:]))
elif opção == 2:
    print('{} convertido para octal é igual a {}'.format(n,oct(n)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida, tente novamente')
