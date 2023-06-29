def validar(letras):
  repeticion=0
  for iteracion in letra:
    if iteracion.isdigit():
      repeticion+=1
  if repeticion>1:
    print("El strig ",letras," tiene numeros")
  else:
    print("El string ",letras," no tiene numeros")

letra=input("Ingrese un string: ")
validar(letra)

