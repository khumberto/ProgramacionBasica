#EJERCICIO 9: Definir una funcion generar n caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar n caracteres(5, "x") deberıa devolver "xxxxx".

def generar_n_caracteres(n, caracter):
    return caracter * n

print(generar_n_caracteres(5, "x"))  
print(generar_n_caracteres(3, "*"))  
print(generar_n_caracteres(0, "a"))  
