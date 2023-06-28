Lista = []
continuar=True
repeticion=0
menor=None
#1
while continuar==True:
  nombre = input("ingrese el nombre que desee: ")
  if nombre=="":# esta solo en comillas refiriendoce a que le dio enter sin ingresar nada
    continuar=False
  else:
    Lista.append(nombre)#si igreso un nombre entonces continua
Tupla=tuple(Lista)#tuple convierte una lista en una tupla
SET=set(Lista)
print(Lista)
print(Tupla)
print(SET)