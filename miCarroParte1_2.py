


####################### Parte 1_2 #######################

print("\nSolicitud de informacion vehicular\n")
print("        Cisco Python Workshop")
usuario = input("\nCual es tu nombre?: ")
marca = input("Que marca es tu auto?: ")
modelo = input("Que sub marca es tu auto? ")
year = 0
placa = input("Placa del vehiculo?: ")

#Comprobar datos guardados
#print(usuario, marca, modelo, year, placa)

#Valores 'input' son interpretados como caracteres en Python
#Presenta como resultado <class 'str'>
#print(type(year))


#Bandera de control de ciclo para conversion numerica
numerico = False


while numerico == False:
    try:
        #Solicitar y convertir a valor numerico la variable 'year')
        year = int(input("Que modelo es tu auto?[1908-2017]: "))

    except:
        print("dato debe ser numerico") #erro si el valor no es numerico
    else:
        #Validacion rango de fechas permitidas
        if (year < 2018) and (year > 1907):
            print("###############################")
            print("      El auto de", usuario)
            print("Es:", marca, "| tipo:", modelo, "| del año:", year)
            print("Con placa de registro:", placa)
            print("Gracias por utilizar este programa")
            numerico = True
        else:
            print("Año fuera de rango")