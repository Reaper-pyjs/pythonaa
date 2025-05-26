al = float(input('Altura da parede: '))
la = float(input('Largura da parede: '))
ar = al * la
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².\nPara pintar essa parede, você precisara de {}l de tinta.'.format(al, la, ar, ar / 2 ))