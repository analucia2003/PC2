#Pregunta 9
#Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio, por ejemplo, omitiendo las vocales.
#Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o minúsculas.

def eliminar_vocales(texto):
    
    vocales = "aeiouAEIOU"
    
    resultado = ''.join([letra for letra in texto if letra not in vocales])
    
    return resultado

entrada = input("Escriba una palabra: ")

salida = eliminar_vocales(entrada)
print(f"Palabra sin vocales: {salida}")

