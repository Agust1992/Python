from Cuadrado import Cuadrado #Sin asterisco solo importamos la clase indicada
from Rectangulo import Rectangulo
from FiguraGeometrica import FiguraGeometrica

print('Creación Objeto Cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(3,'Verde')
print(f'Cálculo del Área del Cuadrado es: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creación Objeto Rectangulo'.center(50,'-'))
rectangulo1 = Rectangulo(2,4,'Rojo')
print(f'Cálculo del Área del Rectangulo es: {rectangulo1.calcular_area()}')
print(rectangulo1)

#No se puede instanciar una clase abstracta
#figura = FiguraGeometrica()


#MRO - Method Resolution Order (Orden de Herencias)
#print(Cuadrado.mro())