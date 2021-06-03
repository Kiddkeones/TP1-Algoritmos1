#Leer tres números, si el segundo es negativo,
#calcular la raíz cuadrada de la suma de los restantes; en caso contrario imprimir un mensaje de error.

numero1=int(input("Ingrese un numero: "))
numero2=int(input("Ingrese otro numero: "))
numero3=int(input("Ingrese el ultimo numero: ")) 
from math import sqrt
if numero1>0 and numero2 >0 and numero3>0:
    print("Error, un numero tiene que ser negativo.")
else:
    suma=(numero1+numero3)
    raiz_cuadrada=sqrt(suma)
    print("Esta es la raiz cuadrada del numero negativo: ", raiz_cuadrada)


