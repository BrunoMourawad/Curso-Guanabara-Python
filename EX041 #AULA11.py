#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
-Até 9 anos: Mirim//-Até 14  anos: Infantil// -Até 19 anos: Junior//-Até 20 anos: Sênior// Acima: Master

id = int(input('Digite a sua idade: '))
if id <= 9:
    print('Sua categoria é mirim.')
    
elif id <= 14:
    print('Sua categoria é infantil.')
    
elif id <= 19:
    print('Sua categoria é junior.')
    
elif id == 20:
    print('Sua categoria é sênior.')
    
else: 
    print('Sua categoria é master.')

