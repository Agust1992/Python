vNum1 = int(input('Ingrese el primer número: '))
vNum2 = int(input('Ingrese el segundo número: '))

if vNum1 > vNum2:
    print(f'El numero mayor es {vNum1}')
elif vNum1 < vNum2:
    print(f'El numero mayor es {vNum2}')
else:
    print('Los números ingresados son idénticos')