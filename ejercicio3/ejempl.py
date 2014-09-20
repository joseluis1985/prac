frase1 = ""
frase2 = ""
cadena = raw_input("Introduce la cadena:   ")
for i in cadena:
  if i.isupper():
      i = i.lower()
  if i != " ":
      frase1 = frase1 + i #creo dos cadenas innecesarias
      frase2 = i + frase2                                                                         
if frase1 == frase2:
  print "true"
else:
  print "false"