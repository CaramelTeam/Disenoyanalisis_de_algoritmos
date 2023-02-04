import sys

unidad = {0:"", 1:"uno",2:"dos",3:"tres",4:"cuatro",5:"cinco",6:"seis",7:"siete",8:"ocho",9:"nueve"}
dec = {0:"", 1:"dieci",2:"veinti",3:"treinta",4:"cuarenta ",5:"cincuenta ",6:"sesenta ",7:"setenta ",8:"ochenta ",9:"noventa"}
especiales = {0:" diez ",1:" once ",2:" doce ",3:" trece ",4:" catorce ",5:" quince ", 6:" veinte "}
cen = {0:"",1:" ciento ", 2:" docientos ", 3:" trecientos ", 4:" cuatrocientos ", 5:" quinientos ", 6:" seiscientos ", 7:" setecientos ", 8:" ochocientos ", 9:" novecientos "}
valor = {1:" mil ", 2:" millones ", 3:" billones "}
acomodo = []

def a_numero(entrada):
    global res_cen
    global res_mil
    for x in entrada:
        numero = int(x) #conversion de la entrada de usuario (string) a entero
        acomodo.append(numero) #funcion para agregar valores al array
        largo = len(acomodo)  #tamaño total del arreglo

    if largo == 9:
        if acomodo[2] == 0:
            if acomodo[5] != 0:
                res_mil = (cen[acomodo[0]] + dec[acomodo[1]] + "y " + unidad[acomodo[2]] + valor[2] + cen[acomodo[3]] + dec[acomodo[4]] + "y " + unidad[acomodo[5]] + valor[1] + cen[acomodo[6]] + dec[acomodo[7]] + "y " + unidad[acomodo[8]])
                return res_mil
            if acomodo[5] == 0:
                res_mil = (cen[acomodo[0]] + dec[acomodo[1]] + "y " + unidad[acomodo[2]] + valor[2] + cen[acomodo[3]] + dec[acomodo[4]] + unidad[acomodo[5]] + valor[1] + cen[acomodo[6]] + dec[acomodo[7]] + unidad[acomodo[8]])
                return res_mil
        if acomodo[1] == 1:
            if acomodo[2] == 0:
                res_mil = (cen[acomodo[0]] + especiales[0] + valor[2] + cen[acomodo[3]] + especiales[0] + valor[1] + cen[acomodo[0]] + especiales[0] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
                return res_mil
            if acomodo[2] == 1:
                res_mil = (cen[acomodo[0]] + especiales[1] + valor[2] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
                return res_mil
            if acomodo[2] == 2:
                res_mil = (cen[acomodo[0]] + especiales[2] + valor[2] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
                return res_mil
            if acomodo[2] == 3:
                res_mil = (cen[acomodo[0]] + especiales[3] + valor[2] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
                return res_mil
            if acomodo[2] == 4:
                res_mil = (cen[acomodo[0]] + especiales[4] + valor[2] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
                return res_mil
            if acomodo[2] == 5:
                res_mil = (cen[acomodo[0]] + especiales[5] + valor[2] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
                return res_mil
        if acomodo[1] == 2:
            if acomodo[0] == 0:
                res_mil = (cen[0] + especiales[6] + valor[1] + cen[acomodo[3]] + dec[acomodo[4]] + unidad[acomodo[5]])
        
    if largo == 8:
        if acomodo[1] == 0:
            res_mil = (dec[acomodo[0]] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
            return res_mil
        if acomodo[0] == 1:
            if acomodo[1] == 0:
                res_mil = (especiales[0] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
                return res_mil
            if acomodo[1] == 1:
                res_mil = (especiales[2] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
                return res_mil
            if acomodo[1] == 2:
                res_mil = (especiales[2] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
                return res_mil
            if acomodo[1] == 3:
                res_mil = (especiales[4] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
                return res_mil
            if acomodo[1] == 4:
                res_mil = (especiales[4] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
                return res_mil
            if acomodo[1] == 5:
                res_mil = (especiales[5] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
                return res_mil
        if acomodo[0] == 2:
            if acomodo[1] == 0:
                res_mil = (especiales[6] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
        
        if acomodo[5] != 0:
            res_mil = (dec[acomodo[0]] + unidad[acomodo[1]] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + "y" + unidad[acomodo[4]])
            return res_mil
        if acomodo[5] == 0:
            res_mil = (dec[acomodo[0]] + unidad[acomodo[1]] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
            return res_mil
    if largo == 7:
        res_mil = (unidad[acomodo[0]] + valor[1] + cen[acomodo[1]] + dec[acomodo[2]] + unidad[acomodo[3]])
        return res_mil
#-------------
    if largo == 6:
        if acomodo[2] == 0:
            if acomodo[5] != 0:
                res_mil = (cen[acomodo[0]] + dec[acomodo[1]] + unidad[acomodo[2]] + valor[1] + cen[acomodo[3]] + dec[acomodo[4]] + "y " + unidad[acomodo[5]])
                return res_mil
            if acomodo[5] == 0:
                res_mil = (cen[acomodo[0]] + dec[acomodo[1]] + unidad[acomodo[2]] + valor[1] + cen[acomodo[3]] + dec[acomodo[4]] + unidad[acomodo[5]])
                return res_mil
        if acomodo[1] == 1:
            if acomodo[2] == 0:
                res_mil = (cen[acomodo[0]] + especiales[0] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
                return res_mil
            if acomodo[2] == 1:
                res_mil = (cen[acomodo[0]] + especiales[1] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
                return res_mil
            if acomodo[2] == 2:
                res_mil = (cen[acomodo[0]] + especiales[2] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
                return res_mil
            if acomodo[2] == 3:
                res_mil = (cen[acomodo[0]] + especiales[3] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
                return res_mil
            if acomodo[2] == 4:
                res_mil = (cen[acomodo[0]] + especiales[4] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
                return res_mil
            if acomodo[2] == 5:
                res_mil = (cen[acomodo[0]] + especiales[5] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
                return res_mil
        if acomodo[1] == 2:
            if acomodo[0] == 0:
                res_mil = (cen[0] + especiales[6] + valor[1] + cen[acomodo[3]] + dec[acomodo[4]] + unidad[acomodo[5]])
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    if largo == 5:
        if acomodo[1] == 0:
            res_mil = (dec[acomodo[0]] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
            return res_mil
        if acomodo[0] == 1:
            if acomodo[1] == 0:
                res_mil = (especiales[0] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
                return res_mil
            if acomodo[1] == 1:
                res_mil = (especiales[2] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
                return res_mil
            if acomodo[1] == 2:
                res_mil = (especiales[2] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
                return res_mil
            if acomodo[1] == 3:
                res_mil = (especiales[4] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
                return res_mil
            if acomodo[1] == 4:
                res_mil = (especiales[4] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
                return res_mil
            if acomodo[1] == 5:
                res_mil = (especiales[5] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
                return res_mil
        if acomodo[0] == 2:
            if acomodo[1] == 0:
                res_mil = (especiales[6] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
        
        if acomodo[5] != 0:
            res_mil = (dec[acomodo[0]] + unidad[acomodo[1]] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + "y" + unidad[acomodo[4]])
            return res_mil
        if acomodo[5] == 0:
            res_mil = (dec[acomodo[0]] + unidad[acomodo[1]] + valor[1] + cen[acomodo[2]] + dec[acomodo[3]] + unidad[acomodo[4]])
            return res_mil
#----------
    if largo == 4:
        res_mil = (unidad[acomodo[0]] + valor[1] + cen[acomodo[1]] + dec[acomodo[2]] + unidad[acomodo[3]])
        return res_mil
#---------------------------------------------------------------------------------------------------------------------------------------------------   
    if largo == 3:
        res_cen = (cen[acomodo[0]] + dec[acomodo[1]] + unidad[acomodo[2]])
        return res_cen
    if largo == 2:
        if acomodo[1] == 0:
            res_cen = (dec[acomodo[0]])
            return res_cen
        if acomodo[0] == 1:
            if acomodo[1] == 0:
                res_cen = (especiales[0])
                return res_cen
            if acomodo[1] == 1:
                res_cen = (especiales[2])
                return res_cen
            if acomodo[1] == 2:
                res_cen = (especiales[2])
                return res_cen
            if acomodo[1] == 3:
                res_cen = (especiales[4])
                return res_cen
            if acomodo[1] == 4:
                res_cen = (especiales[4])
                return res_cen
            if acomodo[1] == 5:
                res_cen = (especiales[5])
                return res_cen
        res_cen = (dec[acomodo[0]] + "y" + unidad[acomodo[1]])
        return res_cen
#------------
    if largo == 1:
        res_cen = (unidad[acomodo[0]])
        return res_cen


#-----------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Necesitas un argumento")
    else:
        num = a_numero(str(sys.argv[1]))
        print("La letra es: ", num)