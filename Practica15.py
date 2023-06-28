def validar(numero):
  if numero.isdigit():
    print("El strig ",numero," tiene numeros")
  else:
    print("El string ",numero," no tiene numeros")

letra=input("Ingrese un string: ")
validar(letra)