"""
Jairo Antonio Melo
2021
GNU

Inputs
Funciones
Creación y lectura de archivos de texto
Imports
"""

def edad(nombre, fecha_de_nacimiento, hoy=2021):
    """
    nombre: es el valor del nombre en texto
    fecha_de_nacimiento: es el año de nacimiento, en integral
    hoy=2021, es posible cambiar la fecha
    """
    edad = hoy - fecha_de_nacimiento
    if edad > 100:
        return "no puedes tener tanto años"
    else:
        return "Hola {}, tu edad es de {}  años".format(nombre, edad)



def hacer_pizza(tamagno, *ingredientes):
    return "pediste una pizza {} con los siguientes ingredientes: {}".format(tamagno, ingredientes)

