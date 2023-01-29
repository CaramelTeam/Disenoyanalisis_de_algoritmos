
import sys

def a_numero(numero):
    numero_en_letra = "setecientos setenta y siete"
    print("El número es:", numero)
    return numero_en_letra
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Necesitas un argumento")
    else:
        num = a_numero(str(sys.argv[1]))
        print("En letra", num)