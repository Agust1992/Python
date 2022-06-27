class Persona:
    def __init__(self, nombre, apellido, edad, *mail, **direcciones):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.mail = mail
        self.direcciones = direcciones

    def imprimir(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.mail}')

if __name__== '__main__': #Condicionamos el bloque, para que no se ejecute al importarse esta clase.
    persona1 = Persona('Juan', 'Acosta', 31, 'juan@udemy.com', Principal='Casa',Secundario='Trabajo')  # Ojeto o Instancia 1
    print(f'Objeto Persona 1: {persona1.nombre},{persona1.apellido}, {persona1.edad},{persona1.mail},{persona1.direcciones}')
    # Modificar Atributos
    persona1.nombre = 'Juan Pablo'
    persona1.imprimir()

    persona2 = Persona('Agus', 'Acosta', 29)  # Ojeto o Instancia 2
    persona2.imprimir()
    # Comparten los atributos de clase, pero con distintos valores.