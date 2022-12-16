#Crie um programa que leia quanto dinheiro ela tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1.00 = R$3.27 
real=float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real/5.27
euro = real/5.20
print('Com R${:.2f} você pode comprar US$ {:.2f}'.format(real, dolar))
print('Com r${:.2f} você pode comprar EUR {:.2f}'.format(real, euro))
