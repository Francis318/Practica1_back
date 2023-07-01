#Escribe un programa tipo "Caja registradora", que permita introducir una lista de artículos, cantidad y precio. Al final debe mostrarle al usuario la cantidad de artículos y la cantidad a cobrar
list=[]
list_items=[]
list_price=[]
continue_operation=True
#1
while continue_operation==True:
  name = input("ingrese el nombre del articulo: ")
  if name=="":
    continue_operation=False
  else:
    list.append(name)
    item1 = input("ingrese la cantidad del articulo: ")
    item2=int(item1)#convertir str a int
    list_items.append(item2)
    price1 = input("ingrese el valor del articulo: ")
    price2=int(price1)#convertir str a int
    list_price.append(price2)
plus_item=0
for item in list_items:
  plus_item+=item

plus_price=0
for item in list_price:
  plus_price+=item

print(list)
print("El total de articulos fueron: ",plus_item)
print("El precio total es de: ",plus_price)