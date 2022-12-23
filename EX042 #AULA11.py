##Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
-Equilátero: Todos os lados iguais//-Isósceles: Dois lados iguais//-Escaleno: todos os lados diferentes

r1 = int(input('Digite o comprimento da primeira reta: '))
r2 = int(input('Digite o comprimento da segunda reta: '))
r3 = int(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2 :
    print('As medidas informadas podem formar um triângulo ',end='')
    if r1 == r2 == r3:
        print('equilátero')
    elif r1 != r2  != r3 !=r1:
        print('escaleno')
    else:
        print('isóceles')
else:
   print('As medidas informadas NÃO podem formar um triângulo. ')


