#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
td = dias*60
tkm = km*0.15
total = td+tkm
print('O valor total pelos dias foi {:.2f}, o valor total pela km foi {:.2f}, o total a pagar é {:.2f}'.format(td,tkm,total))
