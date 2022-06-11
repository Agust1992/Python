"""
#WHILE ASC

vCont = 0
vMax = 5

while vCont <= vMax:
    print(vCont)
    vCont += 1
else:
    print('Contador finalizado')

#WHILE DESC
vCont = 5
vMin = 1
while vCont >= vMin:
    print(vCont)
    vCont = (vCont-1)
else:
    print('Contador finalizado')

##############################################
##FOR 1
##############################################
vCad = 'Holanda'
for letra in vCad:
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break
else:
    print('Fin del For')
"""
vLista = [2018,3,4,5,6,'Fin','River']
len(vLista)
print(len(vLista))
v1 = 0
v2 = 0
for i in vLista:
    if i == 'River':
        v1 = i
    elif i == 2018:
        v2 = i
if v1 == 'River' and v2 == 2018:
    print(f'{v1} en el año {v2} fue el más grande')
