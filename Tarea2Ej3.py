#EJERCICIO 3: Definir una funcion que calcule la longitud de una lista o una cadena dada.

def calcular_longitud(item):
    contador = 0
    for _ in item:
        contador += 1
    return contador
print(calcular_longitud([1, 2, 3, 4, 5]))  
print(calcular_longitud("Hola"))           
print(calcular_longitud(""))              
