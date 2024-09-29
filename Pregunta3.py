#Pregunta 3
#Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
#ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos números.
#Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de números pares e impares.
numeros = []
pares = 0
impares = 0

while True:
    # Preguntamos al usuario si desea ingresar un número
    desea_ingresar = input("¿Quieres dar un número? Responde SI o NO): ").upper()
    
    # Si el usuario responde "NO", terminamos el bucle
    if desea_ingresar == "NO":
        break
    elif desea_ingresar == "SI":
        # Pedimos el número y lo añadimos a la lista
        numero = int(input("Escribe el número: "))
        numeros.append(numero)
        
        # Evaluamos si el número es par o impar
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    else:
        print("Por favor, responda con 'SI' o 'NO'.")

print(f"\nNúmeros ingresados: {numeros}")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
