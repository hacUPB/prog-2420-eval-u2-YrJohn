
#Datos
altitud_inicial = float(input("Ingrese la altitud inicial del satélite (km): "))
coeficiente_arrastre = float(input("Ingrese el coeficiente de arrastre inicial (ej: 0.01): "))
altitud_minima_seguridad = float(input("Ingrese la altitud mínima de seguridad (km): "))

# Variables en 0
altitud_actual = altitud_inicial
orbita = 0  
altitud_perdida = 1 
limite_perdida = 0.001  