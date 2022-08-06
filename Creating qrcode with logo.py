import qrcode
from PIL import Image
Logo_link = input("Give the Link of the Logo which insert: ")
logo = Image.open(Logo_link)
basewidth = 100
wpercent = (basewidth / float(logo.size[0]))
hsize = int((float(logo.size[1]) * float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
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
pos = ((image.size[0] - logo.size[0]) // 2,
       (image.size[1] - logo.size[1]) // 2)
image.paste(logo, pos)
image.save("qrcode.jpg")