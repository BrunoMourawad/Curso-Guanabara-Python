#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math
oposto = float(input('Qual o comprimento do cateto oposto? '))
adjacente = float(input('Qual o comprimento do cateto adjacente? '))
hi = math.hypot(oposto, adjacente)
print('A hipotenusa vai medir {:.2f}'.format(hi))
