#Desenvolva um programa que leia um primeiro termo e a razão de uma progressão aritmética. No final, mostre os 10 primeiros termos dessa progressão.

pt = int(input('Digite o primeiro termo: '))
rz = int(input('Digite a razão: '))
décimo = pt + (10-1) * rz
for c in range(pt,décimo + rz, rz):
    print('{}'.format(c), end=' → ')
print('Acabou')


