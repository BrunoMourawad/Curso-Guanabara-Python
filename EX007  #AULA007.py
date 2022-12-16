#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
s = n1+n2
m = (n1+n2)/2
print ('A soma das notas é {} e a média do aluno é {:.2f}'.format(s,m))
