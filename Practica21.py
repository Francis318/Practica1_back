#Escribe una función que genere una lista con los números de la serie de fibonacci. La función debe recibir la cantidad de números a generar
print("Bienvenido a tu calculadora de number_1s de fibonacci")
def fibonaci(number):
  number_1=0
  previous1=0
  previous2=1
  for i in range(1,number):
    if number_1==0:
      print(previous1)
    number_1=number_1+1
    current=previous1+previous2
    print(current)
    previous2=previous1
    previous1=current

numbers_to_generate = int(input("ingrese el number_1 de number_1s que desee: "))
fibonaci(numbers_to_generate)