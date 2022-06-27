class Aritmetica : #Definimos la clase
    """
    Clase aritmética para operaciones de suma, resta, etc

    """
    def __init__(self,operandoA,operandoB):
        self.operandoA = operandoA #Al atributo le indicamos su parámetro que va a recibir
        self.operandoB = operandoB

    #Definimos los métodos:
    def sumar(self):
        return (self.operandoA+self.operandoB)

    def restar(self):
        return(self.operandoA- self.operandoB)

    def multiplicacion(self):
        return(self.operandoA*self.operandoB)

    def division(self):
        return(self.operandoA/self.operandoB)

vOpeA = int(input('Ingrese el primer operando: '))
vOpeB = int(input('Ingrese el segundo operando: '))

aritmetica1 = Aritmetica(vOpeA,vOpeB) #Creamos el primer Objeto e inicializamos los atributos de la Clase.

print(f'El resultado de la suma es: {aritmetica1.sumar()}')
print(f'EL resultado de la resta es: {aritmetica1.restar()}')
print(f'El resultado de la multiplicación es: {aritmetica1.multiplicacion()}')
print(f'El resultado de la división es: {aritmetica1.division():.3f}') #Le indicamos 3 Decimales