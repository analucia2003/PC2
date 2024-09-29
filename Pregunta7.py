#Pregunta 7
#Escribe un programa que encuentre todos los números perfectos menores que 1000. Un número perfecto es un número entero positivo que es igual a la suma de sus divisores propios positivos
#(excluyendo el propio número).
def es_numero_perfecto(num):
    
    suma_divisores = sum([i for i in range(1, num) if num % i == 0])
    return suma_divisores == num

def numeros_perfectos_menores_de_1000():
    
    numeros_perfectos = []
    for num in range(1, 1000):
        if es_numero_perfecto(num):
            numeros_perfectos.append(num)
    return numeros_perfectos

resultado = numeros_perfectos_menores_de_1000()
print("Números perfectos menores de 1000:")
print(resultado)
