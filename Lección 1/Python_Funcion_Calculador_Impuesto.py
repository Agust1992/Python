###########################################
def CalcImpu (bruto,impuesto):
    total = bruto +bruto * (impuesto/100)
    return total
###########################################
#Ejecutamos la función
bruto = float(input('Ingrese el valor bruto: '))
impuesto = float(input('Ingrese el valor de Impuesto: '))
vValor = CalcImpu (bruto,impuesto)
###########################################
print(f'El valor con impuesto es : {vValor}')