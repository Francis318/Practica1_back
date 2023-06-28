def validar(letras):
  vocales= "aeiouAEIOU"
  if letras in vocales:
    print("El caracter ",letras," es vocal")
  else:
    print("El caracter ",letras," no es vocal")

letra=input("Ingrese una letra: ")
validar(letra)