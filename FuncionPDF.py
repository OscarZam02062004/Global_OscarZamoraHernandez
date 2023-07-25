from reportlab.pdfgen import canvas
ruta="C:/Users/zamor/OneDrive/Escritorio/ModularidadPython/Prueba funciones/"
nombreArchivo=ruta+"reporteGlobal.pdf"
def generarPDF(listaNombres,listaEdades):
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
        yInicial= yInicial-20
    c.save()
    print("--------Reporte generado---------")
