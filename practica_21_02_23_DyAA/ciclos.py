contador = 0
while contador < 6:
    contador += 1
    if contador == 3:
        continue
    print ( contador )


lista_de_frutas = [" manzana ", " platano ", " cereza "]
for fruta in lista_de_frutas :
    print ( fruta )
    if fruta == " platano ":
        break

lista_de_frutas = [" manzana ", " platano ", " cereza "]
for fruta in lista_de_frutas :
    if fruta == " platano ":
        break
    print ( fruta )



lista_de_adjetivos = [" roja ", " grande ", " dulce "]
lista_de_frutas = [" manzana ", "piña", " naranja "]

for adjetivo in lista_de_adjetivos :
    for fruta in lista_de_frutas :
        print ("La", fruta , "es", adjetivo )