#Desenvolva um programa que leia nome, idade e sexo de 4 pessoas, no final o programa deve mostrar a média de idade do grupo, qual o nome do homem mais velho, e quantas mulheres tem menos de 21 anos.

somaidade = 0
midade = 0
maioridadeh = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print('----- {}° PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]:')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
midade = somaidade/4
print ('A média de idade do grupo é de {} anos'.format(midade))
print ('O homem mais velho tem {} anos e se chama {}'.format(maioridadeh, nomevelho))
print('Ao todo temos {} mulher com  menos de 20 anos'.format(totmulher20))







