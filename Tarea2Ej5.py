#EJERCICIO 5: Escribir una funcion sum() y una funcion multip() que sumen y multipliquen respectivamente todos los numeros de una lista. Por ejemplo: sum([1,2,3,4]) deberıa devolver 10 y multip([1,2,3,4]) deberıa devolver 24.

def sum(lista):
    total = 0
    for numero in lista:
        total += numero
    return total

def multip(lista):
    total = 1
    for numero in lista:
        total *= numero
    return total

print(sum([1, 2, 3, 4]))  
print(multip([1, 2, 3, 4]))  
