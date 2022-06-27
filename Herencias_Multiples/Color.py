class Color:
    def __init__(self, color):
        self._color = color         #Encapsulamos con _ antes del argumento

    @property                       #metodo get para recuperar el atributo de color
    def color(self):
        return self._color

    @color.setter                   #Metodo para modificarlo y pasar el valor recibido
    def color(self, color):
        self._color = color         #Al atributo encapsulado le asignamos el nuevo valor

    def __str__(self):              #Sobreescribimos el método
        return f'Color[color: {self._color}]'
