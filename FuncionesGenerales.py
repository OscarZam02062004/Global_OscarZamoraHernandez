from FuncionPDF import *
from DatosEstaticos import *
import os
listaNombres=[]
listaCorreo=[]
listaSueldos=[]
print("Bienvenidos")
print("---------------")
def menu():
    opcion=1
    while(opcion!=0):
        print("1. Usuario existente")
        print("2. Nuevo usuario")
        print("3. Marca del vehiculo")
        print("4. Imprimir Datos")
        print("5. Generar PDF")
        print("6. Generar QR")
        print("7. Listar productos")
        print("0. Salir")
        opcion = int(input("Elige una opcion "))
        os.system('cls')
        if(opcion==1):
            Usuarios()
        elif(opcion==2):
            pedirDatos()
        elif(opcion==3):
            listarCarrosGenerales()
        elif (opcion==4):
            imprimirDatos()
        elif (opcion==5):
            generarPDF(listaNombres,listaCorreo)
        elif (opcion==5):
            listarCarros()

        input("Presiona Enter para continuar...")
        os.system('cls')       

def pedirDatos():
    listaUsuarios.append(input("Ingresa el nombre del usuario:"))
    listaCorreos.append(input("Ingresa un correo electronico:"))
    listaPrecios.append(str(input("Ingresa tu sueldo mensual: ")))
    print("-----------Guardado-------")

def imprimirDatos():
    print('{:<10} {:<20} {:<25} {:>15}'.format("|No|","|Usuario|", "|Correo|", "|Sueldo Mensual|"))
    for i in range (len(listaUsuarios)):
        print('{:<10} {:<20} {:<25} {:<15}'.format(i,listaUsuarios[i],listaCorreos[i],  listaPrecios[i]))
