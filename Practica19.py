#Escribe una función que permita identificar si un número dado es primo o no.
def serch(number):
  posicion=2
  result=0
  while posicion<number and result==0:
    module=number%posicion
    if module==0:
      result+=1
    else:
      posicion+=1
  if result==0:
    print("Tu numero: ",number," es primo")
  else:
    print("Tu numero: ",number," no es primo")

serch_number=int(input("Ingrese un numero para ver si es primo: "))
serch(serch_number)