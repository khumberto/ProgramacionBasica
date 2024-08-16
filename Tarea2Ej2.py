#EJERCICIO 2: Definir una funcion max de tres() que tome tres numeros como argumentos y devuelva el mayor de ellos.

def max_de_tres(a, b, c):
    
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
