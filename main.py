# QR Code Encoding

# Import necessary libraries
import qrcode

# Set date to be encoded in the QR code
data = "Test Data to encode in QR Code"

# Create the QR image
img = qrcode.make(data)

# Save the image to a file
img.save("C:/Users/armyr/OneDrive/Documents/Python/QRCode/qrcode.png")