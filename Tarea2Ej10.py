#EJERCICIO 10: Definir un procedimiento histograma() que tome una lista de n´umeros enteros e imprima un histograma en la pantalla.

def histograma(lista):
    for numero in lista:
        print('*' * numero)

histograma([4, 9, 7]) 
