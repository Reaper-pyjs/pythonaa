salario = float(input('Qual é o salario do Funcionário? R$: '))
aumento = salario + (salario * 15 / 100)
print('Um Funcionário ganhava R${:.2f} passou a ganhar com 15% de aumento R${:.2f}'.format(salario, aumento))