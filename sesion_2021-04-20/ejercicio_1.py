'''
Ejercicio: Con este listado de Estados y capitales, crear un programa que sea capaz
de separar cada entidad y entregar un mensaje para cada Estado que diga:
 
La capital del Estado de Aguascalientes es Aguascalientes
La capital del Estado de Baja California es Mexicali
La capital del Estado de Baja California Sur es La Paz
La capital del Estado de Campeche es San Francisco de Campeche
...
La capital del Estado de Zacatecas es Zacatecas
'''

estados_y_capitales = """Aguascalientes: Aguascalientes, Baja California: Mexicali, Baja California Sur: La Paz, Campeche: San Francisco de Campeche, Chihuahua: Chihuahua, Chiapas: Tuxtla Gutiérrez, Ciudad de México: Ciudad de México, Coahuila: Saltillo, Colima: Colima, Durango: Victoria de Durango, Guanajuato: Guanajuato, Guerrero: Chilpancingo de los Bravo, Hidalgo: Pachuca de Soto, Jalisco: Guadalajara, México: Toluca de Lerdo, Michoacán: Morelia, Morelos: Cuernavaca, Nayarit: Tepic, Nuevo León: Monterrey, Oaxaca: Oaxaca de Juárez, Puebla: Puebla de Zaragoza, Querétaro: Santiago de Querétaro, Quintana Roo: Chetumal, San Luis Potosí: San Luis Potosí, Sinaloa: Culiacán Rosales, Sonora: Hermosillo, Tabasco: Villahermosa, Tamaulipas: Ciudad Victoria, Tlaxcala: Tlaxcala de Xicohténcatl, Veracruz: Xalapa-Enríquez, Yucatán: Mérida, Zacatecas: Zacatecas
"""
import time


e_y_c = estados_y_capitales.split(",")

for e in e_y_c:
    se = e.split(":")
    print(se)
    print("La capital del estado de",se[0],"es",se[1])
    time.sleep(2)



