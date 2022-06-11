class Aritmetica :
    """
    Clase aritmética para operaciones de suma, resta, etc

    """
    def __init__(self,operandoA,operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return (self.operandoA+self.operandoB)

    def restar(self):
        return(self.operandoA- self.operandoB)

    def division(self):
        return(self.operandoA*self.operandoB)

vOpeA = int(input('Ingrese el primer operando: '))
vOpeB = int(input('Ingrese el segundo operando: '))
aritmetica1 = Aritmetica(vOpeA,vOpeB)
print(f'El resultado de la suma es: {aritmetica1.sumar()}')
print(f'EL resultado de l')
print(aritmetica1.division())