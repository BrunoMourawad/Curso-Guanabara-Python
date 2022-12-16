#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros, quilômetros, hectômetros, decâmetros, decímetros 
m = float(input('Digite o valor em metros: '))
cm = m*100 ##Formúla de centímetros
mm = m*1000 ##Formúla de milímetros
hc = m/100 ##Formúla de hectômetros
dc = m/10  ##Formúla de decâmetros
dt = m*10  ##Formúla de decímetros
km = m/1000 ##Formúla de quilômetros

print ('O valor em metros é {}'.format(m))
print ('O valor em centímetros é {}\nO valor em milímetros é {}'.format(cm,mm))
print ('O valor em hectômetros é {}\nO valor em decâmetros é {}'.format(hc,dc))
print ('O valor em decímetros é {}\nO valor em quilômetros é {}'.format(dt,km))
