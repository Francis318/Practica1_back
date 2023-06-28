numero=input("Ingrese un numero:")
while numero.isdigit()!=True:
  print("El dato que ingreso no es valido \n")
  numero=input("Ingrese un numero:")
numero=int(numero)
if numero % 2==0:
    print("Tu numero",numero," es par")
else:
    print("Tu numero",numero," es impar")
