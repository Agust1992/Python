from Persona import Persona #Importamos la Clase al archivo actual

print('Creación Objetos'.center(50,'-'))
persona1 = Persona('Pepe','Acosta',33) #Creamos el Objeto, ingresamos los parámetros
persona1.imprimir() #LLamamos al método de impresión.

print('Eliminación de Objetos'.center(50,'-'))
del persona1
