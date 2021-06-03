#Leer tres números, calcular e imprimir los seis posibles cocientes.


Numero1=int(input("Digite un numero: "))
Numero2=int(input("Digite otro numero: "))
Numero3=int(input("Digite el ultimo numero:"))

cociente1=Numero1/Numero2
cociente2=Numero2/Numero1
cociente3=Numero3/Numero2
cociente4=Numero2/Numero3
cociente5=Numero1/Numero3
cociente6=Numero3/Numero1


print("Esto pueden ser los seis posibles cocientes: ")
print(Numero1,"/",Numero2,"=",cociente1)
print(Numero2,"/",Numero1,"=",cociente2)
print(Numero3,"/",Numero2,"=",cociente3)
print(Numero2,"/",Numero3,"=",cociente4)
print(Numero1,"/",Numero3,"=",cociente5)
print(Numero3,"/",Numero1,"=",cociente6)

