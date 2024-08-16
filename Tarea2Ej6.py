#EJERCICIO 6: Definir una funcion inversa() que calcule la inversion de una cadena. Por ejemplo, la cadena "estoy probando" deberıa devolver la cadena "odnaborp yotse"

def inversa(cadena):
    return cadena[::-1]

cadena_usuario = input("Introduce una cadena para invertir: ")
print("La cadena invertida es:", inversa(cadena_usuario))

