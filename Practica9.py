Lista_numeros=[]
repeticion=0
for iteracion in range(3):
  numero=int(input("Ingrese un numero:"))
  Lista_numeros.append(numero)
for iteracion in Lista_numeros:
  if Lista_numeros.count(iteracion)>1:#count cuenta las veces que pusiste un valor en una lista, si se coloco un valor + de una vez la repeticion se le sumara uno 
    repeticion+=1
if repeticion==3:
  suma=(Lista_numeros[0]+Lista_numeros[1]+Lista_numeros[2])*3
  print("La suma multiplicada por 3 es: ",suma)
elif repeticion<3:
  suma=Lista_numeros[0]+Lista_numeros[1]+Lista_numeros[2]
  print("La suma es: ",suma)
