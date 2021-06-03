if __name__ == '__main__':
	# 1. Leer un numero e imprimirlo junto con sus primeros multiplos, ejemplifique para los primeros 4 multiplos del numero ingresado.
	# el multiplo de un numero es el resultado de la multiplicacion de ese numero con otro
	# Entrada del sistema
	num = float()
	multiplo1 = float()
	multiplo2 = float()
	multiplo3 = float()
	multiplo4 = float()
	print("Ingrese un numero para calcular sus multiplos: ")
	num = float(input())
	# Proceso
	multiplo1 = num*1
	multiplo2 = num*2
	multiplo3 = num*3
	multiplo4 = num*4
	# Salida
	print("Los cuatro primeros multiplos del numero ",num," son:",multiplo1,"/",multiplo2,"/",multiplo3,"/",multiplo4,".")

