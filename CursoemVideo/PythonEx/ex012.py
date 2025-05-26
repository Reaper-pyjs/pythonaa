proço = float(input('Qual é o preço do produto? R$:'))
c = proço * 5 / 100
print('O produto que custava {}, na promoção com desconto de 5% vai custar {:.2f} '.format(proço, proço-c))