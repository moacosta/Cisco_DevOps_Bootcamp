"""
Cisco Python WorkShop

Python Lab 1

Programa para generar una base de datos con informacion de vehiculos aleatorios
dividido en 4 partes:

P1. Solicitar informacion al usuario y presentar datos obtenidos.
        Marca:  Nombre del Fabricante (ej. Audi, VW, Ford)
        Modelo: SubMarca del vehiculo (ej. A4, Jetta, Escape)
        Year:    Año de fabricacion
        Placa:  Placa de identificacion vehicular

        Validar:
        1. Guardar datos en una variable unica
        2. El Año debera ser numerico, no debe ser negativo, entre 1908 y 2017
            1908 año de fabricacion de Ford modelo T

P2. Convertir las condicionales IF en una Funcion que pueda ser utilizada en lo futuro.

P3. Crear una lista para guardar multiples valores, es decir generar una Base de Datos que sera
    exportada a un archivo tipo .CSV como respaldo.
"""

####################### Parte 1_1 #######################

print("\nSolicitud de informacion vehicular\n")
print("        Cisco Python Workshop")
usuario = input("\nCual es tu nombre?: ")
marca = input("Que marca es tu auto?: ")
modelo = input("Que sub marca es tu auto? ")
year = input("Que modelo es tu auto?: ")
placa = input("Placa del vehiculo?: ")

#Comprobar datos guardados
print(usuario, marca, modelo, year, placa)

#Valores 'input' son interpretados como caracteres en Python
#Presenta como resultado <class 'str'>
print(type(year))


#Bandera de control de ciclo para conversion numerica
numerico = False

#Convertir a valor numerico la variable 'year')
while numerico == False:
#Convertir variable 'year' en dato numerico
    try:
        year = int(year)
    #Si el usuario escribio algun caracter el programa anunciara un error y volvera a solicitar la informacion
    except:
        print("Valor de modelo debe ser numerico")
        year = input("\nQue modelo es tu auto?: ")
    #Si el valor fue correcto se continua con la ejecucion
    else:
        numerico = True
        print("dato de Modelo si es numerico\n")


'''
##################################################################################
Inicio
Bloque 1 de Validacion
Utilizando IF anidados

Agregar o eliminar etiquetas de comentario '#' para ejecutar

'''
'''
#Validaciones de variable 'year'#
#Que no sea numero negativo
if year > 0:
    #Que sea mayor a 1907
    if year > 1907:
        #Que sea menor a 2018
        if year < 2018:
            print("###############################")
            print("      El auto de", usuario)
            print("Es:", marca, "| tipo:", modelo, "| del año:", year)
            print("Con placa de registro:", placa)
        else:
            print("El valor de Modelo no es correcto")
            print("debe ser menor a 2018")
            print("vuelva a ejecutar")
    else:
        print(("El valor de Modelo no es correcto"))
        print("debe ser mayor a 1908")
        print("vuelva a ejecutar")
else:
    print(("El valor de Modelo no es correcto"))
    print("debe ser mayor a 0")
    print("vuelva a ejecutar")

print("\nGracias por utilizar este programa")
print("\nFin de Bloque 1")
'''

"""
##################################################################################
Fin
Bloque 1 de Validacion

Agregar o eliminar etiquetas de comentario '#' para ejecutar
"""



"""
##################################################################################
Inicio
Bloque 2 de Validacion
Mismas comprobaciones pero utilizando 'AND' como validacion IF

Agregar o eliminar etiquetas de comentario '#' para ejecutar
"""



if (year > 1907) and (year < 2018):
    print("###############################")
    print("      El auto de", usuario)
    print("Es:", marca, "| tipo:", modelo, "| del año:", year)
    print("Con placa de registro:", placa)
else:
    print(("El valor de Modelo no es correcto"))
    print("debe estar entre el rango 1908 - 2017")
    print("vuelva a ejecutar")

print("\nGracias por utilizar este programa")
print("\nFin de Bloque 2")
'''


##################################################################################
Fin
Bloque 2 de Validacion

Agregar o eliminar etiquetas de comentario '#' para ejecutar
"""

"""
El programa se ejecuta correctamente, sin embargo en las condicionesles 'IF' si el usuario
cometio un error, el programa termina y presenta el mensaje de agradecimiento.

En archivo miCarroParte1_2.py se muestra el codigo agrupando to en un ciclo 'While' que nos permite
preguntar al usuario por los valores de Modelo hasta que sean correctos.
"""

