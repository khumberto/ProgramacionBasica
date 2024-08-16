#EJERCICIO 7: Definir una funcion es palindromo() que reconoce palındromos (es decir, palabras que tienen el mismo aspecto escritas invertidas).Ejemplo: es palindromo("radar") tendrıa ue devolver True.

def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

print(es_palindromo("radar"))       
print(es_palindromo("hola"))       
