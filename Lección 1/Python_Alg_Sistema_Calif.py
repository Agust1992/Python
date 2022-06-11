vNum = int(input('Ingrese un valor entre 0 y 10 : '))
vNota = ''

if vNum >= 9 and vNum <= 10:
    vNota = 'A'
elif vNum >= 8 and vNum <  9:
    vNota = 'B'
elif vNum >= 6 and vNum < 7:
    vNota = 'D'
elif vNum > 0 and vNum < 6:
    vNota = 'F'
else:
    vNota = 'Valor ingresado no válido'

print(f'''
##################################################################################
       Su calificación según la nota {vNum} es: {vNota}
##################################################################################
''')