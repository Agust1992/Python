vEdadAdulto = 18
vEdad = int(input('Ingresa tu edad: '))

if vEdad < vEdadAdulto:
    print (f'Usted es menor de edad, dado que tiene {vEdad} años')
else:
    print (f'Usted tiene mayoría de edad, dado que posee {vEdad} años')