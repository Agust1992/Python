class rectangulo:
    """
    Clase para calculo del Área de Rectángulo
    """

    def __init__(self, base, altura):
        self.base = base  #Al atributo le indicamos su parámetro que va a recibir
        self.altura = altura #Al atributo le indicamos su parámetro que va a recibir

    # Definimos los métodos:
    def rect(self):
        return (self.base * self.altura)


vBase = input('Ingrese la Base del Rectángulo: ')
while not vBase.isdigit(): #Validamos que ingrese un valor numérico
    print('Debe ingresar una Base válida, favor intente de nuevo')
    vBase = input('Ingrese la Base del Rectángulo: ')
vAltura = input('Ingrese la Altura del Rectángulo: ')
while not vAltura.isdigit(): #Validamos que ingrese un valor numérico
    print('Debe ingresas una Altura válida, favor intente de nuevo')
    vAltura = input('Ingrese la Altura del Rectángulo: ')

# Convertimos a Entero las Variables:
vAltura = int(vAltura)
vBase = int(vBase)
# Creamos el Objeto:
rectangulo1 = rectangulo(vBase, vAltura)
#Llamamos al método a partir de nuestro objeto:
print(f'El Área del Rectángulo es: {rectangulo1.rect()}')
