class Vehiculo: #Clase Padre
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'Color: ' + self.color + ',Ruedas :'+str(self.ruedas)

class Coche(Vehiculo): #Clase Hija 1
    def __init__(self,color,ruedas,velocidad):
        super().__init__(color,ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() +', Velocidad máxima en Km/Hs es: '+ str(self.velocidad)

class Bicicleta (Vehiculo): #Clase Hija 2
    def __init__(self,color,ruedas,tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ', y su Tipo es: ' +self.tipo

#Objeto de Clase Vehiculo
vehiculo1 = Vehiculo('Rojo',4)
print(vehiculo1)
#Objeto de Clase Coche
vehiculo2 = Coche('Azul',3,144)
print(vehiculo2)
#Objeto de Clase Bicicleta
vehiculo3 = Bicicleta('Verde',12,'De Montaña')
print(vehiculo3)