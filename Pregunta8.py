#Pregunta 8
#Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La función acepta el número como argumento.
def factorial(n):

    resultado = 1
    
    for i in range(1, n + 1):
        resultado *= i
    
    return resultado

numero = int(input("Escriba un número para hallar su factorial: "))
print(f"El factorial de {numero} es: {factorial(numero)}")
