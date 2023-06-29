Lista = []
continuar=True
repeticion=0
while continuar==True:
  nombre = input("ingrese el nombre que desee: ")
  if nombre=="":# esta solo en comillas refiriendoce a que le dio enter sn ingresar nada
    continuar=False
  else:
    Lista.append(nombre)#si igreso un nombre entonces continua
for item in Lista:
    if Lista.count(item)>1:#count cuenta las veces que pusiste un valor en una lista, si se coloco un valor + de una vez la repeticion se le sumara uno 
      repeticion+=1
print(Lista)
print("Se repito un nombre un total de :",repeticion,"veces")