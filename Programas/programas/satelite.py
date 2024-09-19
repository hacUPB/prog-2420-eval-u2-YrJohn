
#Datos
altitud_inicial = float(input("Ingrese la altitud inicial del satélite (km): "))
coeficiente_arrastre = float(input("Ingrese el coeficiente de arrastre inicial (ej: 0.01): "))
altitud_minima_seguridad = float(input("Ingrese la altitud mínima de seguridad (km): "))

# Variables en 0
altitud_actual = altitud_inicial
orbita = 0  
altitud_perdida = 1 
limite_perdida = 0.001 

#Calculos
while altitud_actual > altitud_minima_seguridad and altitud_perdida > limite_perdida:
    orbita += 1 
    altitud_perdida = coeficiente_arrastre * altitud_actual
    altitud_actual -= altitud_perdida  
    coeficiente_arrastre += 0.0001  
    
#Progreso
    print(f"En la orbita {orbita}, La Altitud es de {altitud_actual}km y la Perdida de altitud es equivalente a  {altitud_perdida}km, Manteniendo un coeficiente de arrastre igual a {coeficiente_arrastre}")

#Final
if altitud_actual <= altitud_minima_seguridad:
    print(f"El satélite ha reingresado en la atmósfera después de {orbita} órbitas.")
else:
    print(f"El satélite se estabilizó a una altitud de {altitud_actual} km después de {orbita} órbitas.")