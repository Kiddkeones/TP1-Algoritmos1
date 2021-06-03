#Leer un número positivo, calcular su cuadrado y su cubo. Imprimir los resultados.

Numero1=int(input("Ingrese un numero: "))

if Numero1>=0:
    potencia_al_cuadrado=Numero1**2
    potencia_al_cubo=Numero1*Numero1*Numero1
    print("Este es su resultado al cuadrado:",potencia_al_cuadrado)
    print("Este es su resultado al cubo:",potencia_al_cubo)
else:
    print("No se puede calcular porque no es un numero positivo")