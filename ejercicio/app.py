# proceso 
#
# acceder al archivo
archivo = open('ejercicio/data/Listado-Instituciones-Educativas-distribuidas-por-zona-distrito-y-circuito.csv', "r")

# obtener las líneas del archivo
lineas = archivo.readlines()

# lineas es ina lista de cadenas
# se imprime las siguientes posiciones
print(lineas[0])
print(lineas[1])

encabezados = lineas[0]
encabezados = encabezados.split("|")
# en línea tomo el valor de lineas[1]
linea = lineas[1]
# a línea que es una cadena, la separo mediante la función
# de Python split
# Recuerdo que el separador de la cadena es un "|"

linea = linea.split("|")

# imprimo la nueva línea; que ahora es una lista
print(linea)

archivo.close()

for Linea in lineas:
  print(Linea)
  pagina = """
  <!DOCTYPE html>
  <html lang="en" dir="ltr">
    <head>
      <meta charset="utf-8">
      <title></title>
    </head>
    <body>
    <b>%s:</b> %s  
    </body>
    </html>
  """ % (encabezados[1], linea[1])

  archivo_generado = open("ejercicio/data/%s.html" % linea[0], "w")
  
  archivo_generado.close()

  print(pagina)


