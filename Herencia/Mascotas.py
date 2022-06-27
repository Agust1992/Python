class Mascotas:
    def __init__(self,nombre,carnet):
        self.nombre = nombre
        self.carnet = carnet

    def __str__(self):
        return f'Mascota [La mascota se llama: {self.nombre}, y su Carnet de Vacunas se encuentra: {self.carnet}]'

class Edades(Mascotas):
    def __init__(self,nombre,carnet,edad):
        super().__init__(nombre,carnet)
        self.edad = edad

    def __str__(self):
        return f'Edad: [Edad: {self.edad}] {super().__str__()} '
