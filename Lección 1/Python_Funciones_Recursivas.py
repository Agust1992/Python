def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero*factorial(numero-1)
################################################################
numero = 5
resultado = factorial(numero)
print(f'El Factorial de {numero} es : {resultado}')

def contadorrecursivo (numero):
    if numero >= 1:
        print (numero)
        contadorrecursivo(numero-1)
    elif numero == 0:
        return
    elif numero <= 0:
        print('Valor incorrecto')
numero = 5
contadorrecursivo(numero)
################################################################