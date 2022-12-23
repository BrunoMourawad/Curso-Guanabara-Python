##Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo com a média atingida:
-Média abaixo de 5.0: Reprovado// - Média entre 5.0 e 6.9: Recuperação// -Média 7.0 ou superior: Aprovado

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
if (n1+n2)/2>=7.0:
    print('Parabéns, você foi aprovado!')
elif (n1+n2)/2>=5.0 and (n1+n2)/2<=6.9:
    print('Sua média foi menor que 7, você está de recuperação!')
elif (n1+n2)/2 < 5.0:
    print('Você está reprovado')



