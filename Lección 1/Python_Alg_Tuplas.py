print('Dada la siguiente tupla, crear lista que solo incluya numeros menores a 5:' )

vTupla = (13,1,8,3,2,5,8)

lista = []
for i in vTupla:
    if i < 5:
       lista.append(i)
print(lista)