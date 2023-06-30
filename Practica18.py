#Escribe una función para verificar que un número se encuentra en un rango de números determinado. El resultado de esa función debe ser booleano
def serch(max,min,serch):
  list=[]
  is_there=False
  if min >= max:
    print('El rango no es el correcto')
  else:
    for number in range(min, max +1):
      list.append(number)
    for number in range(0,len(list)):
      if serch==list[number]:
        is_there=True
      
    print(is_there)

number_min = int(input("ingrese el numero minimo: "))
number_max=int(input("ingrese el numero maximo: "))
serch_number=int(input("ingrese el numero a buscar: "))
args1={
  "max":"number_max",
  "min":"number_min",
  "serch":"serch_number"
}
args1["max"]=number_max
args1["min"]=number_min
args1["serch"]=serch_number
print(args1)
serch(**args1)