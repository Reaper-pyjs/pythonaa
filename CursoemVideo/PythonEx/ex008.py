medida = float(input('Digite quantos metros em centimetro e milimetro : '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
cm = medida * 100
mm = medida * 1000
print('->{}km\n->{}hm\n->{}dam\n->{}m\n->{}cm\n->{}mm'.format(km,hm,dam,medida,cm,mm))