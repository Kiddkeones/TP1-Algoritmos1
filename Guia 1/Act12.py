
# Teniendo como dato la hipotenusa y el angulo que forma esta con la base de un triangulo rectangulo. calcular e imprimir los lados y angulos restantes.
# entrada
# hipotenusa, es una variable
hipotenusa = float()
angulo1 = float()
angulo2 = float()
angulo3 = float()
catetoadyasente = float()
catetoopuesto = float()
# constante, no hay necesidad de definirla
angulo1 = 90
# Proceso
print("ingrese el valor de la hipotenusa:")
hipotenusa = float(input())
print("Ingrese el valor del angulo que forma esta con la base del triangulo rectangulo")
angulo2 = float(input())
angulo3 = 180-(angulo1+angulo2)
catetoadyasente = cos(angulo2)*hipotenusa
catetoopuesto = sin(angulo2)*hipotenusa
# salida
print("Los datos son: hipotenusa: ",hipotenusa," cateto adyasente: ",catetoadyasente," cateto opuesto: ",catetoopuesto," angulos: ",angulo1," ",angulo2," ",angulo3)

