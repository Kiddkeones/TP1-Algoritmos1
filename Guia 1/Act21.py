#Hacer un programa que ingresando como datos:
#a).- Kms. recorridos por un vehículo.
#b).- Precio del combustible por litro.
#c).- Kms. recorridos por cada litro
#a. Calcule:
#a).- La cantidad de litros consumidos b).-Importe gastado en combustible. c).- Imprimir los resultados
#d).- Ejemplificar y realizar la prueba de escritorio

kms_recorridos=int(input("Ingrese el recorrido de su vehiculo: "))
precio_combustible=150
rendimiento_por_litro=15

#Suponiendo que su auto recorre 15km por litro de combustible y el combustible esta a un precio de 150$

cantidad_consumido=(kms_recorridos*rendimiento_por_litro)

combustible_gastado=(precio_combustible*kms_recorridos)/rendimiento_por_litro

print("Esto gastaste en litros:",cantidad_consumido)
print("Esto fue el importe que gastaste en combustible:",combustible_gastado,"Litros")

