O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
n1 = str(input('Aluno 01: '))
n2 = str(input('Aluno 02: '))
n3 = str(input('Aluno 03: '))
n4 = str(input('Aluno 04: '))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem de apresentação é:' )
print(lista)
