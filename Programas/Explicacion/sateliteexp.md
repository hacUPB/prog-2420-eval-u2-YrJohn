#Explicacion-Comentarios
Este codigo fue relativamente mas facil, ya que habian menos procesos a realizar dentro del mismo codigo, cosa que personalmente creia que iba a ser al reves, ya que este era el que mas dificil se veia.


#Codigo parte por partes
1. El codigo inicia pidiendole los datos necesarios para los calculos al usuario.
2. Luego, define las variables en 0 o su valor correspondiente para asi evitar cualquier error a la hora de ejecutarlo.
3. En la tercera parte, utiliza un while para generar un bucle siempre y cuando la altitud sea mayor que la altitud segura.
    #explicacion unno por uno
    1. Utiliza "orbita += 1" para ir dejando en claro las orbitas que van mientras el sistema se ejecuta
    2. "altitud_perdida = coeficiente_arrastre * altitud_actual" calcula la cantidad de altitudd que se pierde.
    3. "altitud_actual -= altitud_perdida " Calcula la altitud a la que queda el satelite en funcion de la altitud perdida.
    4. "coeficiente_arrastre += 0.0001" Aumenta de a muy poco el coeficiente de arrastre para simular la entrada a la atmosfera.
4. De ahi en adelante simplemente saca los calculos de cada uno de manera organizada y que se entienda.