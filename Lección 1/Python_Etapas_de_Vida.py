vEdad = int(input('Proporciona tu Edad: '))
vEtapa = ''

if vEdad >= 0 and vEdad <= 10:
    vEtapa = 'Infancia'
elif vEdad > 10 and vEdad <= 20:
    vEtapa = 'Universidad'
elif vEdad > 20 and vEdad <= 30:
    vEtapa = 'Trabajo'
else:
    vEtapa = 'Etapa no reconocida'

print(f'''
##################################################################################
       Usted se encuentra en la etapa: {vEtapa}
##################################################################################
''')