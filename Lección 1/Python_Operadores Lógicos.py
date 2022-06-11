"""
vNum = int(input('Ingrese un valor numérico: '))
vMin = 0
vMax = 50

if (vNum >= vMin) and (vNum <= vMax):
    print(f'El número ingresado {vNum} está dentro del rango')
else:
    print(f'El número ingresdo {vNum} está fuera de rango')
"""
##################################################################
"""
vVac = False
vDiaDescanso = False

if vVac or vDiaDescanso:
     print ('Puedes tomarte unos días')
else:
    print('Tienes cosas por hacer ok?')
"""
##################################################################
vVac = False
vDiaDescanso = False

if not (vVac or vDiaDescanso):
    print('Tienes cosas por hacer ok?')
else:
    print('Puedes tomarte unos días')