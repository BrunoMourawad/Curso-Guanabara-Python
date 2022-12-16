#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n ** (1/2) #formula de raiz quadrada
print ('O número digitado foi {} \nseu dobro é {} \nseu triplo é {} \ne sua raiz é {:.2f} '.format(n, d, t, r))
