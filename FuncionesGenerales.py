from FuncionPDF import *
from DatosEstaticos import *
import os
listaNombres=[]
listaCorreo=[]
listaSueldos=[]
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
        print("7. Listar productos")
        print("0. Salir")
        opcion = input("Elige una opcion ")
        os.system('cls')
        if(opcion=="1"):
            Usuarios()
        elif(opcion=="2"):
            pedirDatos()
        elif(opcion=="3"):
            Vendedores()
            input("Presiona Enter para continuar...")
            os.system('cls')
            inicio()
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
            imprimirDatos()
        elif (opcion=="5"):
            generarPDF(listaUsuarios,listaPrecios)
        elif (opcion=="6"):
            listarCarros()
        else:
            print("Opcion no valida")

        input("Presiona Enter para continuar...")
        os.system('cls')       

def pedirDatos():
    listaUsuarios.append(input("Ingresa el nombre del usuario:"))
    listaCorreos.append(input("Ingresa un correo electronico:"))
    listaPrecios.append(str(input("Ingresa tu sueldo mensual: ")))
    print("-----------Guardado-------")

def imprimirDatos():
    

def inicio():
    listarCarrosGenerales()
    


