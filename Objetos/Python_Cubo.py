class cubo:
    """
    Clase para calcular Cubos
    """
    def __init__(self,ancho,alto,profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calc_cubo(self):
        return(self.ancho*self.alto*self.profundidad)

vAncho = input('Ingrese el Ancho del Cubo: ')
while not vAncho.isdigit():
    print('Debe ingresar un valor numérico, favor intente de nuevo')
    vAncho = input('Ingrese el Ancho del Cubo: ')

vAlto  = input('Ingrese el Alto del Cubo: ')
while not vAlto.isdigit():
    print('Debe ingresar un valor numérico, favor intente de nuevo')
    vAlto = input('Ingrese el Alto del Cubo: ')

vProf  = input('Ingrese la Profundidad del Cubo: ')
while not vProf.isdigit():
    print('Debe ingresar un valor numérico, favor intente de nuevo')
    vProf = input('Ingrese la Profundidad del Cubo: ')

vAncho = int(vAncho)
vAlto  = int(vAlto)
vProf  = int(vProf)

Cubo1 = cubo(vAncho,vAlto,vProf)
print (f'El volúmen del Cubo ingresado es: {Cubo1.calc_cubo()}')


