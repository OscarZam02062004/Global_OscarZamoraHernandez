import qrcode
ruta="C:/Users/zamor/OneDrive/Escritorio/ModularidadPython/Prueba funciones/"
nombreimagen= ruta+"FuncionQR.png"
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=5)
# qr.add_data(informacion)
qr.make(fit=True)
img=qr.make_image(fill='#000000',back_color=f'#FFFFFF')
f=open(nombreimagen,"wb")
f=open(ruta+"miQR.png","wb")
img.save(f)
f.close()