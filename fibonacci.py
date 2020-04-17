def fibonacci(n):
    """Calcula serie de fibonacci den
    n >2
    return fibonacci(n)
    """
    
    if n == 0 or n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)
    
n=int(input('Escribe tu numero a calcular: '))
save=n
print(f'Resultado de, fibonacci({n})= ',fibonacci(n))
print("Su iteracion fue la siguiente ")
print("**************************************** ")
print('n=', n)
for n in range(n):
    print(f'La sucesion de la serie de Fibonacci de {n} es {fibonacci(n)}')
    print(f'fibonacci({n})= ',fibonacci(n))
print(f'La sucesion de la serie de Fibonacci de {save} es {fibonacci(save)}')
print(f'fibonacci({save})= ',fibonacci(save))