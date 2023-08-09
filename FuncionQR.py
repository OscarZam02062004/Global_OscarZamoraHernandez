import qrcode
#Informacion del QR
def generarQR(nombreQR,informacion):
    print("Entraste al qr")
    img=qrcode.make(informacion)
    f= open(nombreQR,"wb")
    img.save(f)
    f.close()
