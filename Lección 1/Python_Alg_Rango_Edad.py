vEdad = int(input('Ingrese su edad: '))

vMin = 20
vMax = 30

if(vEdad >= vMin and vEdad <= vMax):
    print(f'La edad de {vEdad} años se encuentra dentro del rango')
else:
    print(f'La edad de {vEdad} años supera el rango permitido')
