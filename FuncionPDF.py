from reportlab.pdfgen import canvas
from FuncionQR import *#----QR----
import datetime
import locale
locale.setlocale(locale.LC_ALL,'')
ruta="C:/Users/zamor/OneDrive/Escritorio/ModularidadPython/Prueba funciones/"
nombreQR= ruta+ "miQR.png"#----QR----
def generarPDF(listaUsuarios,listaPrecios):
    fecha_actual=datetime.datetime.now()
    nombreArchivo=ruta+"reporteGlobal"+fecha_actual.strftime('%d-%m-%Y-%H-%M-%S')+".pdf"
    ahora=datetime.datetime.now()
    fecha=ahora.strftime("%Y-%m-%d %H:%M:%S")
    generarQR=(nombreQR,"Hola desde funcion")#----QR----
    c = canvas.Canvas(nombreArchivo)
    xInicial= 200
    yInicial= 700
#----------Datos Generales------------------------
    c.drawString(420,720,f"Fecha: {fecha} ")
#---------------------Imagenes------------------------
    logoDacia= ruta + "LogoDacia.jpg"
    c.drawImage(logoDacia,200,690,200,200, mask="auto")
#-------------------Informacion-----------------------
    c.drawString(50,620,"Estimado(a)")
    """for i in range(len(listaUsuarios)):
        c.setFont('Helvetica',13)

    yInicial=yInicial-20
        c.drawString(xInicial,yInicial,listaPrecios[i])
        c.drawString(xInicial+120,yInicial,listaUsuarios[i])
        c.drawImage(nombreQR,200,400,100,100)#----QR----
        yInicial= yInicial-20"""
    c.save()
    print("--------Reporte generado---------")
