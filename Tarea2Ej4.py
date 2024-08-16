#EJERCICIO 4: Escribir una funcion que tome un caracter y devuelva True si es una vocal, de lo contrario devuelve False.

def es_vocal(caracter):
    vocales = "aeiouAEIOU"
    return caracter in vocales

print(es_vocal("a"))  # Debería devolver True
print(es_vocal("b"))  # Devolverá False
print(es_vocal("E"))  # Debería devolver True
print(es_vocal("z"))  # Devolverá False
