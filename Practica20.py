#Escribe un programa que pueda identificar si una palabra o frase es un palíndromo
def palindromo(word):
  word=word.lower()#Convierte la palabra en minusculas
  word=word.replace(" ","")#Convierte lo que pongas de lado izquierdo a lo que coloques de lado derecho
  first_word=0
  last_word=len(word)-1
  for item in range(first_word,last_word):
    if word[first_word]==word[last_word]:
      first_word+=1
      last_word-=1
    else:
      return False
  return True  

word=input("Ingrese una palabra o frace: ")
if palindromo(word):
  print("Tu palabra: ",word," es palindroma")
else:
  print("Tu palabra: ",word," no es palindroma")