#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500.
s = 0
for c in range (0,500,3):
    if c % 2 > 0:
        s+=c
print('A soma de todos os números múltiplos de 3 que são ímpares no intervalo de 0 a 500 é: {}'.format(s))
