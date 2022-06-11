vLista = [1,2,3,'Jose','Raul','Elias']

for i in vLista:
    if i == 'Elias':
        vLista.append('Pepe')   #Agrego Elemento
        print(vLista)
        vLista.insert(0,'Joel') #inserto valor
        vLista.remove('Raul')   #remuevo valor
        print(vLista)
        del vLista[0]           #Eliminar indicando índice
        print(vLista)
        vLista.clear()          #Eliminar todos los valores de lista
        print(vLista)