#Escribe una función qué reciba varios números y devuelva el mayor de ellos.

    
def big(list):
  bigest=list[0]
  for item in range(0,len(list)):
    if list[item]>bigest:
      bigest=list[item]
  print(bigest)

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
big(list)