
print("Ingrese un numero: ")
entrada = input()
acomodo = []
valor = ["","ciento","cientos","mil","millon"]
unidades = ["","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","diez"]
decenas = ["","diez y ","veinti ", "treinta ","cuarenta ","cincuenta ","sesenta ","setenta ","ochenta ","noventa "]
agregado = "y "
especiales = ["","diez","once","doce","trece","catorce","quince","veinte","cien"]

for x in entrada:
    numero = int(x) #conversion de la entrada de usuario (string) a entero
    acomodo.append(numero) #funcion para agregar valores al array

largo = len(acomodo)  #tamaño total del arreglo


if 3 > largo > 0:
    if largo == 3:
        if acomodo[0] == 1:

            if acomodo[1] == 0:
                if acomodo[2] == 0:
                    final = especiales[8]
                    print("La letra del numero es: ",final)

            if acomodo[1] == 1:
                if acomodo[2] == 0:
                    final = (valor[1] + especiales[1])
                    print("La letra del valor es: ",final)
                if acomodo[2] == 1:
                    final = (valor[1] + especiales[2])
                    print("La letra del valor es: ",final)
                if acomodo[2] == 2:
                    final = (valor[1] + especiales[3])
                    print("La letra del valor es: ",final)
                if acomodo[2] == 3:
                    final = (valor[1] + especiales[4])
                    print("La letra del valor es: ",final)
                if acomodo[2] == 4:
                    final = (valor[1] + especiales[5])
                    print("La letra del valor es: ",final)
                if acomodo[2] == 5:
                    final = (valor[1] + especiales[6])
                    print("La letra del valor es: ",final)
                if acomodo[2] == 6:
                    final = (valor[1] + especiales[7])
                    print("La letra del valor es: ",final)
            if acomodo[1] == 2:
                if acomodo[2] == 0:
                    final = (valor[1] + especiales[7])
                    print("El numero de la letra es: ",final)

            elif acomodo[0] >= 2:
                final1 = (unidades[acomodo[0]] + valor[3])
                final2 = (decenas[acomodo[1]] + agregado + unidades[acomodo[2]])
                final = (final1 + final2)
                print("La letra del numero es: ",final)
if largo == 2:
        if acomodo[0] == 1:
            if acomodo[1] == 0:
                dos = especiales[1]
                print("La letra del numero es: ", dos)
            elif acomodo[1] == 1:
                dos = especiales[2]
                print("La letra del numero es: ", dos)
            elif acomodo[1] == 2:
                dos = especiales[3]
                print("La letra del numero es: ", dos)
            elif acomodo[1] == 3:
                dos = especiales[4]
                print("La letra del numero es: ", dos)
            elif acomodo[1] == 4:
                dos = especiales[5]
        if acomodo[0] == 2:
            final = especiales[7]
            print("La letra del numero es: ",final)
        if acomodo[0] >= 3: 
            if acomodo[1] == 0:
                final =  decenas[acomodo[0]]
        else:
            final =  (decenas[acomodo[0]] + agregado + unidades[acomodo[1]])
            print("La letra del numero es: ", final)
        
        
if largo == 1:
    uno = (unidades[acomodo[0]])
    print("La letra del numero es: ",uno)
if largo == 0:
    print("Tienes que ingresar un nummero")