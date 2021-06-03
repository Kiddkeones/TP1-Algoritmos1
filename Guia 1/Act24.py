#Teniendo como dato el tiempo transcurrido desde el inicio hasta el final de un acontecimiento cualquiera expresado en días,
# hacer los cálculos necesarios e imprimirlo en MINUTOS.

tiempo_transcurrido=int(input("Ingrese el tiempo transcurrido: "))
tiempo_calculado= (tiempo_transcurrido*1440)/1

print(tiempo_transcurrido,"dias son",tiempo_calculado,"en minutos")