def factorial(n):
    """Calcula el factorial de n.

    n int > 0
    returns n
    """
#Descomenta la siguiente linea para ver su comportamiento
    #print(n)
    if n==1:
        return 1
    return n * factorial(n-1)
##Cargamos la pila de fuciones recursivas
##Divide y venceras
n= int(input('Escribe un entero: '))
print(f'el factorial de {n} es =', factorial(n))


