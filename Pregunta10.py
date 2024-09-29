#Pregunta 10
#En los Estados Unidos, las fechas suelen tener el siguiente formato: mes-día-año (MM/DD/AAAA). Las fechas en ese formato no se pueden ordenar fácilmente porque el año de la fecha es el último en
#lugar del primero. Intente ordenar, por ejemplo, 2/2/1800, 3/3/1900 y 1/1/2000 cronológicamente
#en cualquier programa (por ejemplo, una hoja de cálculo). Las fechas en ese formato también son
#ambiguas. ¡Una fecha como el 8 de septiembre de 1636, podría interpretarse como el 9 de agosto de 1636!

def convertir_fecha(fecha):
    

    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    if '/' in fecha:  
        mes, dia, año = fecha.split('/')
    else:  
        partes = fecha.replace(',', '').split()
        mes = str(meses.index(partes[0]) + 1).zfill(2)  
        dia = partes[1].zfill(2)
        año = partes[2]

    mes = mes.zfill(2)
    dia = dia.zfill(2)

    fecha_formateada = f"{año}-{mes}-{dia}"
    return fecha_formateada

fecha_input = input("Escriba una fecha en formato MM/DD/AAAA o 'Mes día, año'): ")

fecha_output = convertir_fecha(fecha_input)
print(f"Fecha en formato AAAA-MM-DD: {fecha_output}")
