#Leer tres números y sumarlos, si la suma es mayor que 10, calcular la raíz cuadrada de la
#suma e imprimirla, de lo contrario, leer dos números más y sumarios junto a los primeros,
#luego imprimir la suma.
from math import sqrt

Num1=int(input("Ingrese un numero: "))
Num2=int(input("Ingrese otro numero: "))
Num3=int(input("Ingrese el ultimo numero: "))

suma=Num1+Num2+Num3

print("Esta es la suma: ", suma)


if suma>10:
    Raiz_cuadrada=sqrt(suma)
    print("Esta es la raiz cuadrada de la suma: ",Raiz_cuadrada)
else:
    print("Como la suma, no llega a 10, sumaremos dos numeros mas:")
    num4=int(input("Ingrese aqui el otro numero: "))
    num5=int(input("Ingrese el ultimo numero: "))
    suma2=Num1+Num2+Num3+num4+num5
    print("Esta es la suma de todos los numeros: ", suma2)