vMes = int(input('Ingrese el mes de la estación (Del 1 al 12): '))
vEstacion = None
if vMes == 1 or vMes == 2 or vMes ==3 :
    vEstacion = 'Verano'
elif vMes == 4 or vMes == 5 or vMes == 6:
    vEstacion = 'Otoño'
elif vMes == 7 or vMes == 8 or vMes == 9:
    vEstacion = 'Invierno'
elif vMes == 10 or vMes == 11 or vMes == 12:
    vEstacion = 'Verano'
else:
    vEstacion = 'Mes ingresado incorrecto'

print(f'''
##################################################################################
       Para el mes {vMes} la estación es --> {vEstacion}
##################################################################################
''')