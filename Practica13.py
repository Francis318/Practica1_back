numero_min=int(input("Ingrese un numero minimo:"))
numero_max=int(input("Ingrese un numero maximo:"))
for iteracion in range(numero_min,numero_max+1):
  if iteracion %3==0:
     print(iteracion)
