from FuncionPDF import *
from DatosEstaticos import *
import os
import time
import sys
print("Bienvenidos a la concecionaria Dacia")
print("---------------")
def menu():
    opcion=1
    while(opcion!=0):
        print("1. Usuario existente")
        print("2. Nuevo usuario")
        print("3. Vendedor que te va entender")
        print("4. Imprimir Datos de usuarios existentes")
        print("5. Generar PDF")
        print("6. Generar QR")
        print("7. Garantia por defecto o premium")
        print("8.Pago en efectivo o en tarjeta")
        print("9. Salir")
        opcion = input("Elige una opcion ")
        os.system('cls')
        if(opcion=="1"):
            #Usuarios()
            Personalizacion_Usuario()
        elif(opcion=="2"):
            pedirDatos()
        elif(opcion=="3"):
            Vendedores()
            input("Presiona Enter para continuar...")
            os.system('cls')
            listarCarrosGenerales()
            input("Presiona Enter para continuar...")
            os.system('cls')
            print("Bienvenido a la personalizacion de tu vehiculo")
            print("-------------------------------------")
            listarColores()
            input("Presiona Enter para continuar...")
            os.system('cls')
            listarColoresInteriores()
            input("Presiona Enter para continuar...")
            os.system('cls')
            tipoTransmicion()
            input("Presiona Enter para continuar...")
            os.system('cls')
            tiposRines()
            input("Presiona Enter para continuar...")
            os.system('cls')
        elif (opcion=="4"):
            Impresion_Usuarios_Existentes()
        elif (opcion=="5"):
            generarPDF(listaUsuarios,listaPrecios)
        elif (opcion=="6"):
            generarQR()
        elif(opcion=="7"):
            Garantia()
        elif(opcion=="8"):
            Pago()
        else:
            print("Opcion no valida")

        input("Presiona Enter para continuar...")
        os.system('cls')       

def pedirDatos():
    listaUsuarios.append(input("Ingresa el nombre del usuario:"))
    listaCorreos.append(input("Ingresa un correo electronico:"))
    listaPrecios.append(str(input("Ingresa tu sueldo mensual: ")))
    print("-----------Guardado-------")

def Garantia():
    print("1.Por defecto")
    print("2.Premium")
    valor=input("Ingrese la opcion que desee: ")
    if valor=="1":
        print("Cada 15,000 km  o 1 año lo que suceda primero")
    elif valor=="2":
        print("2 años extendida sin limite de kilometraje")
    else:
        print("Opcion no valida")

def Pago():
    total=float(input("Ingrese el costo del vehiculo: "))
    print("1.Pago en efectivo")
    print("2.Pago con tarjeta")
    pago=input("¿Como pagaras? ")
    if pago=="1":
        PagoEfectivo=float(input("Ingrese la cantidad de efectivo: "))
        if PagoEfectivo>=total:
            print("Cobro exitososo disfrute su vehiculo")
        else:
            print("No le alcanza jefe")
    elif pago=="2":
        mensaje = "Procesando el pago con tarjeta.........."
        duracion = 5
        intervalo = 1  
        parpadeo(mensaje, duracion, intervalo)
        print("Pago con tarjeta exitoso")
    else:
        print("Opcion no valida")
#---------Datos extras---------------------
def parpadeo(mensaje, duracion, intervalo):
    iteraciones = int(duracion / intervalo)
    for _ in range(iteraciones):
        sys.stdout.write("\r" + mensaje)
        sys.stdout.flush()
        time.sleep(intervalo)
        
        sys.stdout.write("\r" + " " * len(mensaje))
        sys.stdout.flush()
        time.sleep(intervalo)
    sys.stdout.write("\r" + mensaje + "\n")
    sys.stdout.flush()
                       
