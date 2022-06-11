def convertidor_a_farenheit (farenheit): #Defino la función
    vFar = ((farenheit*9/5)+32) #Armo la fórmula
    return vFar #Retorno el valor
###############################################################
farenheit = int(input('Ingrese los grados que desea convertir: ')) #Solicito el input
valor = convertidor_a_farenheit (farenheit) #Llamo la función
print(f'La conversión a farenheit de {farenheit} grados es {valor}')
###############################################################
def convertidor_a_grados (grados): #Defino la función
    vGrados = ((grados-32)*5/9)#Armo la fórmula
    return vGrados#Retorno el valor
###########################################
grados = int(input('Ingrese los farenheit que desea convertir: '))#Solicito el input
valor = convertidor_a_grados (grados)
print(f'La conversión a grados de {grados} farenheit es {valor}')