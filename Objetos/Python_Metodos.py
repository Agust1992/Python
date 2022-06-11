class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrarDetalle(self):  #Metodo De Instancia
        print(f'Persona {self.nombre}, {self.apellido},{self.edad}')

persona1 = Persona('Juan','Acosta',31)#Ojeto o Instancia 1
persona1.mostrarDetalle()
#Otra forma de llamar al método, indicando el objeto
#Persona.mostrarDetalle(persona1)
persona1.mail = 'juan@udemy.com' #Podemos agregar atributos propios de un objeto
print(persona1.mail)

persona2 = Persona('Agus','Acosta',29) #Ojeto o Instancia 2
persona2.mostrarDetalle()