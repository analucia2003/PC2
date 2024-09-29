#Pregunta 4
#Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
#pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
#materias.

# Lista para almacenar los datos de los alumnos
alumnos = []

# Pedimos al usuario que ingrese la cantidad de alumnos
n = int(input("Ingrese la cantidad de alumnos: "))

# Iteramos para ingresar los datos de cada alumno
for _ in range(n):
    # Creamos un diccionario para el alumno
    alumno = {}
    
    # Pedimos el nombre del alumno
    alumno['Alumno'] = input("Ingrese el nombre del alumno: ")
    
    # Pedimos las tres notas del alumno y las guardamos en una lista
    notas = []
    for i in range(1, 4):
        nota = int(input(f"Ingrese la nota {i} del alumno {alumno['Alumno']}: "))
        notas.append(nota)
    
    # Guardamos las notas en el diccionario del alumno
    alumno['Notas'] = notas
    
    # Añadimos el diccionario del alumno a la lista de alumnos
    alumnos.append(alumno)

# Mostramos la lista completa de alumnos con sus notas
print("\nListado de Alumnos y sus Notas:")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")
