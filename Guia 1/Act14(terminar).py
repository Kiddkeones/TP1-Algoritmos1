#Ingresar por teclado un lado y la hipotenusa de un triángulo rectángulo, 
#calcular e imprimir el lado restante, la superficie y los ángulos de dicho triángulo.
from math import sqrt

lado=int(input("Ingrese un Lado de su triangulo: "))
hipotenusa=int(input("Ingrese su Hipotenusa: "))


lado_restante=sqrt(hipotenusa**2 - lado**2)
print("Este es su lado restante: ",lado_restante)


superficie= lado*lado_restante/2
print("Este es la superficie: ",superficie)


