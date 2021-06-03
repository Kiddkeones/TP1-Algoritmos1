#Si un lote de terreno tiene X metros de frente por Y metros de fondo: calcular e imprimir la
#cantidad de metros de alambre para cercarlo. (X e Y serán leídos al comenzar el programa)

#Variable de entrada
X1=int(input("Ingrese metros de frente: "))
Y1=int(input("Ingrese metros de fondo: "))
#Proceso
Cerca=(X1*2)+(Y1*2)
#salida
print("Perimetro: ",Cerca)
