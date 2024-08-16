#EJERCICIO 8: Definir una funcioon superposicion() que tome dos listas y devuelva True si tienen al menos un miembro en comun o devuelva False de lo contrario. Escribir la funcion usando el bucle for anidado.

def superposicion(lista1, lista2):
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                return True
    return False

print(superposicion([1, 2, 3], [4, 5, 6])) 
print(superposicion([1, 2, 3], [3, 4, 5]))  
print(superposicion(['a', 'b', 'c'], ['d', 'b', 'e']))  
