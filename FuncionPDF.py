from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4 
from DatosEstaticos import *
from FuncionQR import *#----QR----
import datetime
import locale
import random
locale.setlocale(locale.LC_ALL,'')
w, h = A4
def generarPDF():
    ruta="C:/Users/zamor/OneDrive/Escritorio/ModularidadPython/Prueba_funciones/"
    nombreQR= ruta+ "ejemploQR.png"#----QR----
    fecha_actual=datetime.datetime.now()
    nombreArchivo=ruta+"reporteGlobal"+fecha_actual.strftime('%d-%m-%Y-%H-%M-%S')+".pdf"
    ahora=datetime.datetime.now()
    fecha=ahora.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Lista: {listarCarros}")
    generarQR(nombreQR,"Hola desde funcion")#----QR----
    c = canvas.Canvas(nombreArchivo)
    for i in range(len(listarCarros)):
        xInicial= 200
        yInicial= 700
    #----------Datos Generales------------------------
        c.drawString(420,720,f"Fecha: {fecha} ")
    #---------------------Imagenes------------------------
        logoDacia= ruta + "LogoDacia.jpg"
        c.drawImage(logoDacia,200,690,200,200, mask="auto")
    #-------------------Informacion-----------------------
        c.drawString(50,620,"Estimado(a)")
        c.drawString(50,580,"Le agradecemos su interés por los productos exclusivos de la concecionaria Dacia y por")
        c.drawString(50,560,"realizar la configuración personalizada de su vehículo en el Dacia Car Configurator.")
        c.drawString(50,540,"La concecionaria Dacia es exponente de la conducción deportiva. Nuestros vehículos no ")
        c.drawString(50,520,"sólo representan una innovación sin compromisos, ya que la combinación de valores")
        c.drawString(50,500,"tradicionales con características deportivas, tecnología, diseño, agilidad y seguridad,")
        c.drawString(50,480,"integran una unidad armoniosa que está presente en cada modelo.")
        c.drawString(50,450,"Esperamos que su configuración personal sea de su agrado. La oferta es un resumen sin")
        c.drawString(50,430,"compromisos basada en el precio público informativo del modelo y las opciones elegidas.")
        c.drawString(50,410,"También puede guardar su configuración personalizada o bien enviarla directamente al")
        c.drawString(50,390,"concesionario.")
        c.drawString(50,350,"Reciba un cordial saludo")
        c.drawString(50,330,"Atte:Dacia")
    #--------------Pagina 1---------
    #-------------Informacion del carro-------
        c.showPage()
        logoDacia= ruta + "LogoDacia.jpg"
        c.drawImage(logoDacia,200,690,200,200, mask="auto")
        x = 0 
        y = h - 160 
        c.line(x, y, x + 800, y)
        c.setFont("Helvetica-Bold",20)
        c.drawString(230,660,"Datos Tecnicos")
        x = 0 
        y = h - 400 
        c.line(x, y, x + 800, y)
        c.setFont("Helvetica",13)
        c.drawString(50,640,"Motor: ")
        c.drawString(50,620,"No.Cilindros: ")
        c.drawString(50,590,"Potencia: ")
        c.drawString(50,570,"Velocidad maxima del motor: ")
        c.drawString(50,550,"Rendimiento de combustible: ")
        c.drawString(50,530,"Velocidad de 0 a 100 km: ")
    #------------Informacion del carro--------
    #---------Garantia y personalizacion------
        c.setFont("Helvetica-Bold",20)
        c.drawString(250,410,"Garantia")
        c.setFont("Helvetica",13)
        c.drawString(50,390,"Tipo de garantia que escogio: ")
        x = 0 
        y = h - 600
        c.line(x, y, x + 800, y)
        c.setFont("Helvetica",13)
        c.drawString(50,370,"Modelo:"+listarCarros[i])
        numero_random_transmicion=random.randint(0,1)
        c.drawString(50,350,"Tipo de transmicion:"+Transmicion[numero_random_transmicion])
        numero_random_color=random.randint(0,9)
        c.drawString(50,330,"Color exterior del vehiculo:"+Colores[numero_random_color])
        numero_random_colorint=random.randit(0,3)
        c.drawString(50,310,"Color interior del vehiculo: "+ColorInteriores[numero_random_colorint])
        numero_random_Rines=random.randit(0,2)
        c.drawString(50,290,"Tipo de rin:"+Rines[numero_random_Rines])
        c.showPage()
    #---------Garantia y personalizacion------

        """for i in range(len(listaUsuarios)):
            c.setFont('Helvetica',13)

        yInicial=yInicial-20
            c.drawString(xInicial,yInicial,listaPrecios[i])
            c.drawString(xInicial+120,yInicial,listaUsuarios[i])
            c.drawImage(nombreQR,200,400,100,100)#----QR----
            yInicial= yInicial-20"""
    c.save()
    print("--------Reporte generado---------")


def generarReporteVenta(Personalizacion_Final):
    ruta="C:/Users/zamor/OneDrive/Escritorio/ModularidadPython/Prueba_funciones/"
    nombreQR= ruta+ "ejemploQR.png"#----QR----
    fecha_actual=datetime.datetime.now()
    nombreArchivo=ruta+"reporteVentaAuto"+fecha_actual.strftime('%d-%m-%Y-%H-%M-%S')+".pdf"
    ahora=datetime.datetime.now()
    fecha=ahora.strftime("%Y-%m-%d %H:%M:%S")
    print("ENtro al qr")
    generarQR(nombreQR,"Hola desde funcion")#----QR----
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
    c.drawString(50,580,"Le agradecemos su interés por los productos exclusivos de la concecionaria Dacia y por")
    c.drawString(50,560,"realizar la configuración personalizada de su vehículo en el Dacia Car Configurator.")
    c.drawString(50,540,"La concecionaria Dacia es exponente de la conducción deportiva. Nuestros vehículos no ")
    c.drawString(50,520,"sólo representan una innovación sin compromisos, ya que la combinación de valores")
    c.drawString(50,500,"tradicionales con características deportivas, tecnología, diseño, agilidad y seguridad,")
    c.drawString(50,480,"integran una unidad armoniosa que está presente en cada modelo.")
    c.drawString(50,450,"Esperamos que su configuración personal sea de su agrado. La oferta es un resumen sin")
    c.drawString(50,430,"compromisos basada en el precio público informativo del modelo y las opciones elegidas.")
    c.drawString(50,410,"También puede guardar su configuración personalizada o bien enviarla directamente al")
    c.drawString(50,390,"concesionario.")
    c.drawString(50,350,"Reciba un cordial saludo")
    c.drawString(50,330,"Atte:Dacia")
#--------------Pagina 1---------
    c.showPage()
    logoDacia= ruta + "LogoDacia.jpg"
    c.drawImage(logoDacia,200,690,200,200, mask="auto")
    x = 0 
    y = h - 160 
    c.line(x, y, x + 800, y)
    c.setFont("Helvetica-Bold",20)
    c.drawString(230,660,"Datos Tecnicos")
    x = 0 
    y = h - 400 
    c.line(x, y, x + 800, y)
    c.setFont("Helvetica",13)
    c.drawString(50,640,"Motor: ")
    c.drawString(50,620,"No.Cilindros: ")
    c.drawString(50,590,"Potencia: ")
    c.drawString(50,570,"Velocidad maxima del motor: ")
    c.drawString(50,550,"Rendimiento de combustible: ")
    c.drawString(50,530,"Velocidad de 0 a 100 km: ")
    c.setFont("Helvetica-Bold",20)
    c.drawString(250,410,"Garantia")
    c.setFont("Helvetica",13)
    c.drawString(50,390,"Tipo de garantia que escogio: ")
    x = 0 
    y = h - 600
    c.line(x, y, x + 800, y)
    c.setFont("Helvetica",13)
    c.drawString(50,370,"Modelo:"+Personalizacion_Final[0])
    c.drawString(50,350,"Tipo de transmicion: "+Personalizacion_Final[1])
    c.drawString(50,330,"Color exterior del vehiculo: "+Personalizacion_Final[2])
    c.drawString(50,310,"Color interior del vehiculo: "+Personalizacion_Final[3])
    c.drawString(50,290,"Tipo de rin: "+Personalizacion_Final[4])


    c.save()
    print("--------Reporte generado---------")