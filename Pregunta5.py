#Pregunta 5
#Escribe un programa que encuentre la suma de todos los números primos menores que 100.
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def suma_primos_menores_100():
    suma = 0
    for num in range(2, 100):
        if es_primo(num):
            suma += num
    return suma

resultado = suma_primos_menores_100()
print(f"La suma de todos los números primos menores que 100 es: {resultado}")
