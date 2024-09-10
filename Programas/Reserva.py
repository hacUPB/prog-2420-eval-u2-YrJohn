
#Nombre del viajero
Nombre = input("Ingrese su nombre completo: ")
print (f"¡Bienvenido a FastFast Airlines, {Nombre}!")
#Rutas
origen = input("Ingrese su ciudad de origen (Medellín, Bogotá o Cartagena): ")
destino = input("Ingrese su ciudad de destino (Medellín, Bogotá o Cartagena): ")
dia_semana = input("Ingrese el día de la semana (lunes, martes, etc.): ")
dia_mes = int(input("Ingrese el día del mes (1-30): "))

#Distancias
distancias = {"Medellín-Bogotá": 240, "Medellín-Cartagena": 461, "Bogotá-Cartagena": 657}
ruta = origen + "-" + destino
distancia = distancias[ruta]

#Precios
precio = 79900 if dia_semana in ["lunes", "martes", "miércoles", "jueves"] and distancia < 400 else \
        119900 if dia_semana not in ["lunes", "martes", "miércoles", "jueves"] and distancia < 400 else \
        156900 if dia_semana in ["lunes", "martes", "miércoles", "jueves"] else 213000

# Asignación de asiento
preferencia = input("Prefiere asiento en el pasillo, ventana o no tiene preferencia? ")
asiento = "C" if preferencia == "pasillo" else "A" if preferencia == "ventana" else "B"
numero_asiento = random.randint(1, 29)







#Reserva
print(f"""
Aqui esta su reserva:
Nombre: {Nombre}
origen: {origen}
destino: {destino}
fecha: {dia_semana} {dia_mes}
precio: ${precio}
asiento: {numero_asiento}{asiento}
""")
