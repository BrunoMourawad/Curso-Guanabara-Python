#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
-Abaixo de 18.5: Abaixo do peso//-Entre 18.5 e 25: Peso ideal//-25 até 30: Sobrepeso//30 até 40: Obesidade//-Acima de 40: Obesidade mórbida

import math
alt = float(input('Digite seu altura: '))
peso = float(input('Digite a sua peso: '))
imc = peso/(alt**2)
if imc < 18.5:
    print('O seu imc é {:.2f} você está abaixo do peso. '.format(imc))
elif imc >= 18.5 and imc <= 24.99:
    print('O seu imc é {:.f} seu peso está ideal. '.format(imc))
elif imc >= 25 and imc < 30:
    print('O seu imc é {:.2f} você está com sobrepeso. '.format(imc))
elif imc >= 30 and imc <= 40:
    print('O seu imc é {:.2f} você está obeso. '.format(imc))
elif imc > 40:
    print('O seu imc é {:.2f} você está com obesidade mórbida. '.format(imc))
