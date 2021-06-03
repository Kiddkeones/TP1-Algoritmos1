#Leer dos números reales, calcular e imprimir los dos posibles cocientes entre ellos.
#Int=entero
#Input=Entrada por teclado
#ejemplo:Variable1=int(input("Parametro")) --> 

print ("Ingrese Dos numeros reales")
#Entrada
Numero1=int(input("Ingrese un numero: "))
Numero2=int(input("Ingrese otro numero: "))
#proceso
Cociente=Numero1/Numero2
Cociente2=Numero2/Numero1

#Salida
print ("Este es un posible cociente entre ellos: ")
print (Numero1,"/",Numero2,":",Cociente)

print ("Este es otro posible cociente entre ellos: ")
print (Numero2,"/",Numero1,":",Cociente2)
