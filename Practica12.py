repeticion=0
Lista_de_nombres=["Karen","Karla","Marcos","Dani"]
print(Lista_de_nombres)
nombre = input("ingrese el nombre que desee: ")
Lista_de_nombres.append(nombre)
print(Lista_de_nombres)

for item in Lista_de_nombres:
    if Lista_de_nombres.count(item)>1:
      repeticion+=1
      
print(repeticion)

if repeticion>0:
  print("Tu nombre esta repetido: ",nombre)
else:
  print("Tu nombre no esta repetido: ",nombre)
