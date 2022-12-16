#FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E LEIA O SEU NOVO PREÇO COM 5% DE DESCONTO.
preco =float(input('Digite o preço do produto: R$'))
desc = preco-(preco*5/100)
print('O valor total do produto com 5% de desconto é: {}'.format(desc))
