import qrcode

def generar_codigo_qr(dato,nombre_archivo):
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(dato)
    qr.make(fit=True)

    img=qr.make_image(fill_color="black",back_color="white")
    img.save(nombre_archivo+".png")

datos_para_qr="https://www.python.org/"    
nombre_archivo="codigo_qr"

generar_codigo_qr(datos_para_qr,nombre_archivo)