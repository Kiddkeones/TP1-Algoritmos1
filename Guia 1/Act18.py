#Calcular la velocidad de un móvil que se desplaza con velocidad constante conociendo el espacio recorrido
#y el tiempo empleado en recorrerle (los datos serán leídos al comenzar el programa)

distancia=float(input("Ingrese la distancia recorrida en kilometros: "))
tiempo=float(input("Cual fue el tiempo que recorrio en horas: "))

velocidad=distancia/tiempo

print(f"La velocidad fue {velocidad} Km/H")
