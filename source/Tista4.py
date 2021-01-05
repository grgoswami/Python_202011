import qrcode 
from PIL import Image

#Link
link = input("Enter a link : ")
fillc = input("Choose a color for the QR code : ")
backc = input("Choose a color for the background : ")

qr = qrcode.QRCode(
    box_size=15,
    border=4,
)

qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill_color = fillc, back_color = backc).convert('RGB')
img.save("QR.png")
img.show()


#Email
email = input("Enter a email : ")
fillc = input("Choose a color for the QR code : ")
backc = input("Choose a color for the background : ")

qr = qrcode.QRCode(
    box_size=15,
    border=4,
)

qr.add_data("mailto: " + email)
qr.make(fit=True)

mail = qr.make_image(fill_color = fillc, back_color = backc).convert('RGB')
mail.save("QR.png")
mail.show()