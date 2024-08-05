import qrcode as qr
img = qr.make("https://www.linkedin.com/in/dhiraj-kumar-317b08228/")
img.save("linkedin.png")
