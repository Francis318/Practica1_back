#Escribe una función que permita multiplicar varios números
def multi(list):
  number=1
  for item in list:
    number*=item
  print(number)


continue_op=True
list=[]
while continue_op==True:
  number = input("ingrese el number que desee: ")
  if number=="":
      continue_op=False
  else:
    new_number=int(number)#convertir str a int
    list.append(new_number) 

print(list)
multi(list)