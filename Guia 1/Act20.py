#Ingresar como dato el perímetro de un cuadrado.
#Calcular e imprimir el volumen del cubo que tiene como lado el cuadrado antes mencionado.

perimetro=int(input("Ingrese el perimetro de su cuadrado: "))

calcular_lado=perimetro/4

volumen=calcular_lado*calcular_lado*calcular_lado

print("Este es el lado del cuadrado: ",calcular_lado)
print("Este es su volumen de un cuadrado: ",volumen)
