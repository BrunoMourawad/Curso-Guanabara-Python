#Escreva um programa que leia uma temperatura em graus c e converta para f
c = float(input('Informe  a temperatura em °C:'))
f = ((9 * c) / 5) + 32
print('A temperatura de {}°C corresponde a {} em°F!'.format(c, f))
