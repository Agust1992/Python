class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def get_nombre(self):
        print("Llamando método get nombre")
        return self._nombre

    def set_nombre(self, nombre):
        print("Llamando método set nombre")
        self._nombre = nombre

    def mostrar_detalle(self):
        print(f"Persona: {self._nombre} {self.apellido} - Edad: {self.edad}")


persona_1 = Persona("Bart", "Simpson", 10)
print(persona_1._nombre)

# Aquí estoy usando los métodos set_nombre y get_nombre para modificar y recuperar la información del atributo _nombre
persona_1.set_nombre("Cornelio del Rancho")
print(persona_1.get_nombre())