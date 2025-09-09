#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
import math
radio=float(input("Ingrese el radio del cirulo"))
area = math.pi *(radio**2)
perimetro = 2* math.pi * radio
print(f"el area del ciruclo es:{area:.2f} y su perimetro {perimetro:.2f}")