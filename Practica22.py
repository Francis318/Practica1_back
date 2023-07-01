#Escribe un programa que emule el funcionamiento de una calculadora simple.
print("python3 calculator.py")
continue_operation=True
var=0
while continue_operation==True:
  if var==0:
    number1=int(input(": "))
    print(number1)
    var+=1
  elif var>0:
    number2=input(": ")
    if number2=="":
      print("adios")
      continue_operation=False
    else:
      operation_plus=number2.count("+")
      operation_rest=number2.count("-")
      operation_division=number2.count("/")
      operation_multiply=number2.count("*")
      #print(operation_plus) 
      #print(operation_rest)  
      #print(operation_division)  
      #print(operation_multiply)
      number2=number2.replace("+","")
      number2=number2.replace("-","")
      number2=number2.replace("/","")
      number2=number2.replace("*","")
      number2=int(number2)
      if operation_plus>0:
        result=number1+number2
        print(result)
        number1=result
      elif operation_rest>0:
        result=number1-number2
        print(result)
        number1=result
      elif operation_division>0:
        result=number1/number2
        print(result)
        number1=result
      elif operation_multiply>0:
        result=number1*number2
        print(result)
        number1=result
      elif number2=="":
        continue_operation=False
      