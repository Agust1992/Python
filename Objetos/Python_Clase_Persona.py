class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


persona1 = Persona('Pepe','Acosta',28)
print(f'Objeto Persona1 --> {persona1.nombre} {persona1.apellido} {persona1.edad}')

persona2 = Persona('Juan','Acosta',30)
print(f'Objeto Persona2 --> {persona2.nombre} {persona2.apellido} {persona2.edad}')