#Dados dos lados de un triángulo, calcular la hipotenusa mediante Pitágoras.


print("Ingrese los lados de su triangulo:")

lado1=int(input("Ingrese aca su lado: "))
lado2=int(input("Ingrese el otro lado: "))

hipotenusa=(lado1**2 +lado2**2)**(1/2)  

print("Este es resultado de la hipotenusa",hipotenusa)