#Dado un número entero positivo menor que cien, leerlo desde teclado, indicar si es primo.

numero_primo= True

numero=int(input("Digite un numero menor a 100: "))

if numero < 100 and numero > 0:
    for n in range (2, numero):
        if numero%n == 0:
            numero_primo= False
            break
else:
    print("Error, numero negativo o mayor a 100.")

if numero_primo == True:
        print(f"{numero} es un numero primo.")
else:
    print(f"{numero} no es un numero primo, {n} es divisor.")