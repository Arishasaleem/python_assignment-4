import qrcode

data = input("Enter the text or URL to encode in QR: ")

qr = qrcode.make(data)

qr.save("my_qr.png")
print("✅ QR code saved as 'my_qr.png'")
