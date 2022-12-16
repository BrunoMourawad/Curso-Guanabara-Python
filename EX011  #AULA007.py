#Faça um programa que leia a altura e a largura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2 metros quadrados.
lg = float(input('Digite a largura da parede: '))
at = float(input('Digite a altura da parede: '))
area = lg*at
tinta = area/2
print ('A sua parede tem dimensão de {}x{} e sua área é de {}m²'.format(lg, at, area))
print ('Para pintar a parede você irá precisar de {} litros de tinta'.format(tinta))
