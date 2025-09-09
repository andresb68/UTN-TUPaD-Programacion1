#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
a=int(input("Ingrese el primer numero entero"))
b=int(input("Ingrese el segundo numero"))
print(f"Suma: {a + b}")
print(f"Resta (a - b): {a - b}")
print(f"Resta (b - a): {b - a}")
print(f"Multiplicación: {a * b}")

if b != 0:
    print(f"División (a / b): {a / b:.2f}")
else:
    print("División (a / b): indefinida (no se puede dividir por cero)")

if a != 0:
    print(f"División (b / a): {b / a:.2f}")
else:
    print("División (b / a): indefinida (no se puede dividir por cero)")