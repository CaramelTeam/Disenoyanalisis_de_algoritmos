def mil_millones():
    fijo4 = "mil"
    fijo5 = "millones"
    if largo == 12:
        if acomodo[0] == 1:
            prefijo1 = "ciento"
        if acomodo[0] == 2:
            prefijo1 = "doscientos"
        if acomodo[0] == 3:
            prefijo1 = "trescientos"
        if acomodo[0] == 4:
            prefijo1 = "cuatrocientos"
        if acomodo[0] == 5:
            prefijo1 = "quinientos"
        if acomodo[0] == 6:
            prefijo1 = "seiscientos"
        if acomodo[0] == 7:
            prefijo1 = "setecientes"
        if acomodo[0] == 8:
            prefijo1 = "ochocientos"
        if acomodo[0] == 9:
            prefijo1 = "novecientos"

def millones(largo):
        if largo == 9:
            if acomodo[0] == 1:
                prefijo1 = "ciento"
            if acomodo[1] == 0:
                if acomodo[2] == 0:
                    prefijo1 == "cien"
            if acomodo[0] == 2:
                prefijo1 = "doscientos"
            if acomodo[0] == 3:
                prefijo1 = "trescientos"
            if acomodo[0] == 4:
                prefijo1 = "cuatrocientos"
            if acomodo[0] == 5:
                prefijo1 = "quinientos"
            if acomodo[0] == 6:
                prefijo1 = "seiscientos"
            if acomodo[0] == 7:
                prefijo1 = "setecientes"
            if acomodo[0] == 8:
                prefijo1 = "ochocientos"
            if acomodo[0] == 9:
                prefijo1 = "novecientos"
            return prefijo1

def mil(largo):
    fijo1 = mil
    if largo == 6:
            if acomodo[0] == 0:
                prefijo1 = ""
            if acomodo[0] == 1:
                prefijo1 = "ciento"
            if acomodo[0] == 1:
                if acomodo[1] == 0:
                    if acomodo[2] == 0:
                        prefijo1 == "cien"
            if acomodo[0] == 2:
                prefijo1 = "doscientos"
            if acomodo[0] == 3:
                prefijo1 = "trescientos"
            if acomodo[0] == 4:
                prefijo1 = "cuatrocientos"
            if acomodo[0] == 5:
                prefijo1 = "quinientos"
            if acomodo[0] == 6:
                prefijo1 = "seiscientos"
            if acomodo[0] == 7:
                prefijo1 = "setecientes"
            if acomodo[0] == 8:
                prefijo1 = "ochocientos"
            if acomodo[0] == 9:
                prefijo1 = "novecientos"
        #-------------------------------------------------
        if largo == 5:
                if acomodo[0] == 0:
                    prefijo2 == ""
                if acomodo[0] == 1:
                    if acomodo[1] == 0:
                        prefijo2 == "diez"
                    if acomodo[1] == 1:
                        prefijo2 == "once"
                    if acomodo[1] == 2:
                        prefijo2 == "doce"
                    if acomodo[1] == 3:
                        prefijo2 == "trece"
                    if acomodo[1] == 4:
                        prefijo2 == "catorce"
                    if acomodo[1] == 5:
                        prefijo2 == "quince"
                    if acomodo[1] == 6:
                        prefijo2 == "diez y seis"
                    if acomodo[1] == 7:
                        prefijo2 == "diez y siete"
                    if acomodo[1] == 8:
                        prefijo2 == "diez y ocho"
                    if acomodo[1] == 9:
                        prefijo2 == "diez y nueve"
            #-----------------------------------------
        if largo == 5:
            if acomodo[0] == 2:
                if acomodo[1] == 0:
                    prefijo5 == "Veinte"
            #-----------------------------------------
            if acomodo[0] == 2:
                prefijo5 = "Veinti"
                complit = ""
            if acomodo[0] == 3:
                prefijo5 = "treinta"
                complit = "y"
            if acomodo[0] == 4:
                prefijo5 = "cuarenta"
                complit = "y"
            if acomodo[0] == 5:
                prefijo5 = "cincienta"
                complit = "y"
            if acomodo[0] == 6:
                prefijo5 = "sesenta"
                complit = "y"
            if acomodo[0] == 7:
                prefijo5 = "setenta"
                complit = "y"
            if acomodo[0] == 8:
                prefijo5 = "ochenta"
                complit = "y"
            if acomodo[0] == 9:
                prefijo5 = "noventa"
                complit = "y"
            #----------------------------------------
        if largo == 4:
            if acomodo[0] == 1:
                prefijo4 = "uno"
            if acomodo[0] == 2:
                prefijo4 = "dos"
            if acomodo[0] == 3:
                prefijo4 = "tres"
            if acomodo[0] == 4:
                prefijo4 = "cuatro"
            if acomodo[0] == 5:
                prefijo4 = "cinco"
            if acomodo[0] == 6:
                prefijo4 = "seis"
            if acomodo[0] == 7:
                prefijo4 = "siete"
            if acomodo[0] == 8:
                prefijo4 = "ocho"
            if acomodo[0] == 9:
                prefijo4 = "nueve"

            return prefijo1, prefijo2, complit, prefijo3
#--------------------------------------------------------------------------------------------------------------------------------------------------------#
        if largo == 3:
            if acomodo[0] == 0:
                prefijo1 = ""
            if acomodo[0] == 1:
                prefijo1 = "ciento"
            if acomodo[0] == 1:
                if acomodo[1] == 0:
                    if acomodo[2] == 0:
                        prefijo1 == "cien"
            if acomodo[0] == 2:
                prefijo1 = "doscientos"
            if acomodo[0] == 3:
                prefijo1 = "trescientos"
            if acomodo[0] == 4:
                prefijo1 = "cuatrocientos"
            if acomodo[0] == 5:
                prefijo1 = "quinientos"
            if acomodo[0] == 6:
                prefijo1 = "seiscientos"
            if acomodo[0] == 7:
                prefijo1 = "setecientes"
            if acomodo[0] == 8:
                prefijo1 = "ochocientos"
            if acomodo[0] == 9:
                prefijo1 = "novecientos"
        #-------------------------------------------------
        if largo == 2:
                if acomodo[0] == 0:
                    prefijo2 == ""
                if acomodo[0] == 1:
                    if acomodo[1] == 0:
                        prefijo2 == "diez"
                    if acomodo[1] == 1:
                        prefijo2 == "once"
                    if acomodo[1] == 2:
                        prefijo2 == "doce"
                    if acomodo[1] == 3:
                        prefijo2 == "trece"
                    if acomodo[1] == 4:
                        prefijo2 == "catorce"
                    if acomodo[1] == 5:
                        prefijo2 == "quince"
                    if acomodo[1] == 6:
                        prefijo2 == "diez y seis"
                    if acomodo[1] == 7:
                        prefijo2 == "diez y siete"
                    if acomodo[1] == 8:
                        prefijo2 == "diez y ocho"
                    if acomodo[1] == 9:
                        prefijo2 == "diez y nueve"
            #-----------------------------------------
                if acomodo[0] == 2:
                    if acomodo[1] == 0:
                        prefijo2 == "Veinte"
            #-----------------------------------------
                if acomodo[0] == 2:
                    prefijo2 = "Veinti"
                    complit = ""
                if acomodo[0] == 3:
                    prefijo2 = "treinta"
                    complit = "y"
                if acomodo[0] == 4:
                    prefijo2 = "cuarenta"
                    complit = "y"
                if acomodo[0] == 5:
                    prefijo2 = "cincienta"
                    complit = "y"
                if acomodo[0] == 6:
                    prefijo2 = "sesenta"
                    complit = "y"
                if acomodo[0] == 7:
                    prefijo2 = "setenta"
                    complit = "y"
                if acomodo[0] == 8:
                    prefijo2 = "ochenta"
                    complit = "y"
                if acomodo[0] == 9:
                    prefijo2 = "noventa"
                    complit = "y"
                #----------------------------------------
        if largo == 1:
            if acomodo [0] == 0:
                prefijo3 == ""
            if acomodo[0] == 1:
                prefijo3 = "uno"
            if acomodo[0] == 2:
                prefijo3 = "dos"
            if acomodo[0] == 3:
                prefijo3 = "tres"
            if acomodo[0] == 4:
                prefijo3 = "cuatro"
            if acomodo[0] == 5:
                prefijo3 = "cinco"
            if acomodo[0] == 6:
                prefijo3 = "seis"
            if acomodo[0] == 7:
                prefijo3 = "siete"
            if acomodo[0] == 8:
                prefijo3 = "ocho"
            if acomodo[0] == 9:
                prefijo3 = "nueve"

            return prefijo1, prefijo2, complit, prefijo3


def cien(largo, acomodo):
        if largo == 3:
            if acomodo[0] == 0:
                prefijo1 = ""
            if acomodo[0] == 1:
                prefijo1 = "ciento"
            if acomodo[0] == 1:
                if acomodo[1] == 0:
                    if acomodo[2] == 0:
                        prefijo1 == "cien"
            if acomodo[0] == 2:
                prefijo1 = "doscientos"
            if acomodo[0] == 3:
                prefijo1 = "trescientos"
            if acomodo[0] == 4:
                prefijo1 = "cuatrocientos"
            if acomodo[0] == 5:
                prefijo1 = "quinientos"
            if acomodo[0] == 6:
                prefijo1 = "seiscientos"
            if acomodo[0] == 7:
                prefijo1 = "setecientes"
            if acomodo[0] == 8:
                prefijo1 = "ochocientos"
            if acomodo[0] == 9:
                prefijo1 = "novecientos"
        #-------------------------------------------------
        if largo == 2:
                if acomodo[0] == 0:
                    prefijo2 == ""
                if acomodo[0] == 1:
                    if acomodo[1] == 0:
                        prefijo2 == "diez"
                    if acomodo[1] == 1:
                        prefijo2 == "once"
                    if acomodo[1] == 2:
                        prefijo2 == "doce"
                    if acomodo[1] == 3:
                        prefijo2 == "trece"
                    if acomodo[1] == 4:
                        prefijo2 == "catorce"
                    if acomodo[1] == 5:
                        prefijo2 == "quince"
                    if acomodo[1] == 6:
                        prefijo2 == "diez y seis"
                    if acomodo[1] == 7:
                        prefijo2 == "diez y siete"
                    if acomodo[1] == 8:
                        prefijo2 == "diez y ocho"
                    if acomodo[1] == 9:
                        prefijo2 == "diez y nueve"
            #-----------------------------------------
        if largo == 2:
            if acomodo[0] == 2:
                if acomodo[1] == 0:
                    prefijo2 == "Veinte"
            #-----------------------------------------
            if acomodo[0] == 2:
                prefijo2 = "Veinti"
                complit = ""
            if acomodo[0] == 3:
                prefijo2 = "treinta"
                complit = "y"
            if acomodo[0] == 4:
                prefijo2 = "cuarenta"
                complit = "y"
            if acomodo[0] == 5:
                prefijo2 = "cincienta"
                complit = "y"
            if acomodo[0] == 6:
                prefijo2 = "sesenta"
                complit = "y"
            if acomodo[0] == 7:
                prefijo2 = "setenta"
                complit = "y"
            if acomodo[0] == 8:
                prefijo2 = "ochenta"
                complit = "y"
            if acomodo[0] == 9:
                prefijo2 = "noventa"
                complit = "y"
            #----------------------------------------
        if largo == 1:
            if acomodo [0] == 0:
                prefijo3 == ""
            if acomodo[0] == 1:
                prefijo3 = "uno"
            if acomodo[0] == 2:
                prefijo3 = "dos"
            if acomodo[0] == 3:
                prefijo3 = "tres"
            if acomodo[0] == 4:
                prefijo3 = "cuatro"
            if acomodo[0] == 5:
                prefijo3 = "cinco"
            if acomodo[0] == 6:
                prefijo3 = "seis"
            if acomodo[0] == 7:
                prefijo3 = "siete"
            if acomodo[0] == 8:
                prefijo3 = "ocho"
            if acomodo[0] == 9:
                prefijo3 = "nueve"

            return prefijo1, prefijo2, complit, prefijo3


print("Ingrese un numero: ")

entrada = input()
acomodo = []

for x in entrada:
    numero = int(x) #conversion de la entrada de usuario (string) a entero
    acomodo.append(numero) #funcion para agregar valores al array
    largo = len(acomodo)  #tamaño total del arreglo

    if 12 > largo > 9:
        mil_millones(largo, acomodo)
    if 9 > largo > 6:
        millones(largo)
    if 6 > largo > 3:
        mil(largo)
    if 3 > largo > 0:
        cien(largo)
    if largo == 0:
        print("Tienes que ingresar un nummero")