"""
try :
    x = input()
    print ( x)
except NameError :
    print ("La variable x no esta definida ")
except ZeroDivisionError:
    print (" Algo más salio mal ")
except :
    print("Este es otro error")
"""

"""
try :
 print (" Hola ")
except :
 print (" Algo salio mal")
else :
 print (" Nada salio mal")
"""

"""
try :
 print ( x )
except :
 print (" Algo salio mal")
finally :
 print ("El bloque de 'try except ' ha terminado ")
 """

"""
try :
    f = open ("demo.txt","x") #(, "w") sirve para crar el archivo
    try :
        f.write(" Algún texto ... ")
    except :
        print (" Algo salio mal al escribir en el archivo ")
    finally :
        f.close ()
except :
    print (" Algo salio mal al abrir el archivo ")
"""
"""
x = -1

if x < 0:
    raise Exception ("Lo siento , no se permiten nú meros menores a cero ")

"""

x = " hello "

if not type ( x ) is int:
    raise TypeError (" Solo enteros son permitidos ")