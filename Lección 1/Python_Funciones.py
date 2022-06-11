def Mi_Funcion (Nombre,Apellido):
    print(f'Nombre: {Nombre}, Apellido: {Apellido}')

Mi_Funcion('Pepe', 'Acosta')

def sumando(a,b):
    return a+b

vValor1 = input('Ingrese número entero a sumar: ')
while not vValor1.isdigit(): #Validamos que se informe un valor numérico
	print('Debe ingresar un valor numérico, intente de nuevo')
	vValor1 = input('Ingrese número entero a sumar: ')

vValor2 = input('Ingrese el segundo valor entero a sumar: ')
while not vValor2.isdigit():#Validamos que se informe un valor numérico
	print('Debe ingresar un valor numérico, intente de nuevo')
	vVar2 = input('Ingrese un número entero a sumar: ')

vValor1 = int(vValor1) #Convertimos a tipo entero
vValor2 = int(vValor2) #Convertimos a tipo entero

resultado =sumando(vValor1,vValor2) #Ejecutamos la función, pasamos los argumentos
print(f'El resultado de la suma es: {resultado}')