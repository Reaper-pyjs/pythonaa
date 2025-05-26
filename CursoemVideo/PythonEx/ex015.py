#obs: o preços do dia de alugueu e 60 de km rodado é 0.15 isso é so treino de progamacão
dia = int(input('Quantos dia vocé alugou o carro?: '))
km = float(input('Quantos km vocé andou?: '))
d = dia * 60
k = km * 0.15
print('Vocé vai pagar de dia como o carro é R${:.2f} e de km rodado é R${:.2f} no total dar R${:.2f}'.format(d, k, d + k))