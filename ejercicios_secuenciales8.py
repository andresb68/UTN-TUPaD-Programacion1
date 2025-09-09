#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 

altura=float(input("Ingrese un su altura en mts"))
peso=float(input("Ingrese su peso en kg"))
imc= peso/(altura)**2
print(f"Su IMC es de:{imc:.2f}%")