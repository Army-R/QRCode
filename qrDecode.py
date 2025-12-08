# QR Code Decoding

# Import necessary libraries
from pyzbar.pyzbar import decode
from PIL import Image

# Open the image
img = Image.open('qrcode.png')
# Decode the QR code
result = decode(img)
# Print the decoded data
print(result[0].data.decode('utf-8'))
