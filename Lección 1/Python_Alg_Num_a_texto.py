vNum = int(input('Ingrese un valor entre 1 y 3: '))
vNumText = ''
if vNum == 1:
    vNumText = 'Número uno'
elif vNum == 2:
    vNumText = 'Número dos'
elif vNum == 3:
    vNumText = 'Número tres'
else:
    vNumText = 'No se encuentra entre los valores 1 al 3'

print(f'''
##################################################################################
        Número proporcionado: {vNum} - {vNumText}
##################################################################################
''')