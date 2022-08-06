import qrcode
QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
qr = qrcode.QRCode(
    version =1,
    box_size =10,
    border=6)
data = input("The data for qr code : ")
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill_color="black", back_color= "white")
image.save("qrcode.jpg")