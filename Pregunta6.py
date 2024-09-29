#Pregunta 6
#Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
def fibonacci_hasta_50():
    a, b = 0, 1
    fibonacci = []
    
    while a <= 50:
        fibonacci.append(a)
        a, b = b, a + b
    
    return fibonacci

# Llamada a la función y mostrar el resultado
resultado = fibonacci_hasta_50()
print("Serie de Fibonacci entre 0 y 50:")
print(resultado)
