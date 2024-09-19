import random

def seleccionar_opcion(opciones):
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    seleccion = int(input("Seleccione una opción (número): "))
    while seleccion < 1 or seleccion > len(opciones):
        seleccion = int(input("Opción inválida. Seleccione un número válido: "))
    return opciones[seleccion - 1]




#Nombre del viajero
print("Seleccione su titulo:")
titulos = ["Sr.", "Sra."]
titulo = seleccionar_opcion(titulos)


Nombre = input("Ingrese su nombre completo: ")
print (f"¡Bienvenido a FastFast Airlines, {titulo}{Nombre}!")

#Rutas
# Seleccionar origen
print("Seleccione su ciudad de origen:")
ciudades = ["Medellín", "Bogotá", "Cartagena"]
origen = seleccionar_opcion(ciudades)

# Seleccionar destino
print("Seleccione su ciudad de destino:")
destino = seleccionar_opcion(ciudades)
while destino == origen:
    print("El destino no puede ser igual al origen. Seleccione otro destino.")
    destino = seleccionar_opcion(ciudades)

#Seleccionar día semana
print("Seleccione el día de la semana:")
dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
dia_semana = seleccionar_opcion(dias_semana)


#Seleccionar mes
print("Seleccione el mes de su viaje:")
Meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
Mes = seleccionar_opcion(Meses)

#Seleccionar día mes
dia_mes = int(input("Ingrese el día del mes (1-30): "))
while dia_mes < 1 or dia_mes > 30:
    dia_mes = int(input("Día inválido. Ingrese un número entre 1 y 30: "))
#Distancias
distancias = {"Medellín-Bogotá": 240, "Medellín-Cartagena": 461, "Bogotá-Cartagena": 657}
ruta = origen + "-" + destino
if ruta not in distancias:
    ruta = destino + "-" + origen
distancia = distancias[ruta]

#Precios
precio = 79900 if dia_semana in ["lunes", "martes", "miércoles", "jueves"] and distancia < 400 else \
        119900 if dia_semana not in ["lunes", "martes", "miércoles", "jueves"] and distancia < 400 else \
        156900 if dia_semana in ["lunes", "martes", "miércoles", "jueves"] else 213000

#Asientos
print("Seleccione su preferencia de asiento:")
preferencias_asiento = ["pasillo", "ventana", "sin preferencia"]
preferencia = seleccionar_opcion(preferencias_asiento)
asiento = "C" if preferencia == "pasillo" else "A" if preferencia == "ventana" else "B"
numero_asiento = random.randint(1, 29)







#Reserva
print(f"""
Su reserva fue realizada con exito:
Reserva para: {titulo}{Nombre}
Viaja desde: {origen}
Viaja hacia: {destino}
Dia de su viaje: {dia_semana} {dia_mes} de {Mes}
Precio de su boleto: ${precio}
Su asiento: {numero_asiento}{asiento}
¡Gracias por confiar en FastFast Airlines!
""")
