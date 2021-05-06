import random

def generar_contrasena(): #Funcion
    mayusculas = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] #CREACION DE LISTAS DE LETRAS Y CARACTERES
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    simbolos = ['!', '#', '$', '&', '/', '(', ')']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayusculas + minusculas + simbolos + numeros  #SUMAR LISTAS EN UNA LISTA UNICA 

    contrasena =[] #LISTA VACIA PARA PONER LOS CARACTERES ALEATORIOS

    for i in  range(15):
        caracter_random = random.choice(caracteres) #se elige un caracter al azar y se guarda
        contrasena.append(caracter_random) #se agrega el caracter random a la lista contrasena

    contrasena = "".join(contrasena) #convertir lista a str 
    return contrasena


def main():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es : ' + contrasena) 

if __name__ == '__main__':
    main()