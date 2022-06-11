print('Proporcione los siguientes datos del Libro')
vTitulo = input('Ingrese el nombre del Libro: ')
vId = int(input('Ingrese el Id numérico del Libro: '))
vPrecio = float(input('Ingrese el precio del Libro: '))

vEnvio = input('Indique si el envío es gratuito (TRUE/FALSE): ')
if vEnvio == 'True':
    vEnvio = 'El envío es gratuito'
elif vEnvio == 'False':
     vEnvio='Envío es con recargo'
else:
    print('Ingrese valor distinto de nulo')


print(f'''
################################################
        Nombre del Libro:       {vTitulo}         
        El Id del Libro es:     {vId}
        El Precio del Libro es: {vPrecio}
        Modo de envío es:       {vEnvio}
################################################
''')


