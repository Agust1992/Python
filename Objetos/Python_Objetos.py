class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


persona1 = Persona('Juan','Acosta',31)#Ojeto o Instancia 1
print(f'Objeto Persona 1: {persona1.nombre},{persona1.apellido}, {persona1.edad}')
#Modificar Atributos
persona1.nombre = 'Juan Pablo'
print(f'Objeto Persona 1: {persona1.nombre},{persona1.apellido}, {persona1.edad}')


persona2 = Persona('Agus','Acosta',29) #Ojeto o Instancia 2
print(f'Objeto Persona 2: {persona2.nombre},{persona2.apellido}, {persona2.edad}')
#Comparten los atributos de clase, pero con distintos valores.