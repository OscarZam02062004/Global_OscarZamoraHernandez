from reportlab.pdfgen import canvas
from FuncionQR import *#----QR----
import datetime
import locale
locale.setlocale(locale.LC_ALL,'')
ruta="C:/Users/zamor/OneDrive/Escritorio/ModularidadPython/Prueba funciones/"
nombreQR= ruta+ "miQR.png"#----QR----
def generarPDF(listaNombres,listaEdades):
    fecha_actual=datetime.datetime.now()
    nombreArchivo=ruta+"reporteGlobal"+fecha_actual.strftime('%d-%m-%Y-%H-%M-%S')+".pdf"
    generarQR(nombreQR,"Hola desde funcion")#----QR----
    c = canvas.Canvas(nombreArchivo)
    xInicial= 200
    yInicial= 700
    c.drawString(xInicial,yInicial,"Edad")
    c.drawString(xInicial+120,yInicial,"Nombre")
    for i in range(len(listaNombres)):
        c.setFont('Helvetica',13)
        yInicial=yInicial-20
        c.drawString(xInicial,yInicial,listaEdades[i])
        c.drawString(xInicial+120,yInicial,listaNombres[i])
        c.drawImage(nombreQR,200,400,100,100)#----QR----
        yInicial= yInicial-20
    c.save()
    print("--------Reporte generado---------")
