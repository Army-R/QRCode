# QR Code Encoding

# Import necessary libraries
import qrcode

# Create the QR code
data =  "https://github.com/Army-R" # Data to be encoded
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_H,
    box_size=15,
    border=7,
)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="blue", back_color="white")

# Save the image to a file
img.save("qrcode.png")