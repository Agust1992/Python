class Persona: #Creamos la Clase Padre
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self): #Metodo en clase padre para imprimir valores
        return f'Persona[Nombre: {self.nombre}, Edad: {self.edad}]'

class Empleado(Persona): #Creamos la Clase Hija
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):#Metodo en clase padre para imprimir valores
        return f'Empleado[Sueldo: {self.sueldo}] {super().__str__()} '#Com super accedemos a Metodos/Atr Padres

