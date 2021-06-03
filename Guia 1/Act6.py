#Un pintor sabe que con una pintura determinada puede pintar 3,6 metros cuadrados por cada medio litro. 
# Sabiendo la altura y el largo de la pared a pintar, informar cuántos litros de pintura utilizará.
# (Altura y Largo en metros).

Altura_pared=int(input("Escriba la altura de la Pared: "))
Largo_pared=int(input("Escriba el largo de la pared: "))

Calculo_area_pared= Altura_pared* Largo_pared

Calculo_de_pintura= (Calculo_area_pared*0.5) / 3.6

print("Utilizara", round(Calculo_de_pintura,2),"Litros de pintura.")