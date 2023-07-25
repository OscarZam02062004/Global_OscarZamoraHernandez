from reportlab.pdfgen import canvas
ruta="C:/Users/zamor/OneDrive/Escritorio/ModularidadPython/Prueba funciones/"
nombreArchivo=ruta+"reporteGlobal.pdf"
def generarPDF():
    c = canvas.Canvas(nombreArchivo)
    c.drawString(200,600,"Hola desde una funcion")
    c.save()
    print("--------Reporte generado---------")
