from math import pow,sqrt
cateto1 = int(input('Qual o valor do primeiro cateto: '))
cateto2 = int(input('Qual o valor do segundo cateto: '))
rc1 = pow(cateto1,2)
rc2 = pow(cateto2,2)
hipotenusa = rc1 + rc2
rh = sqrt(hipotenusa)
perimetro = rc1 + rc2 + rh
print(f'{rc1}  {rc2}  {rh} ')