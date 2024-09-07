
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
ruta = origen  +"-"+  destino
distancia = distancias[ruta]
