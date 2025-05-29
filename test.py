import math
a = float(input('o termo A da função? '))
b = float(input('o termo B da função? '))
if b < 0:
    b = -1*b
    raiz = a/b
    print(raiz)

else: 
    if b > 0:
        b = -1*b 
        raiz = (a/b)
        print(raiz)