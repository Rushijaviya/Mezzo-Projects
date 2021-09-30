# pip install pyqrcode
# pip install pypng 
import pyqrcode
import png
from pyqrcode import QRCode


# Take user input website which represents the QR code
print("Enter website to make QR Code")
s=input()

# Generate QR code
url = pyqrcode.create(s)

# Create the svg file 
url.svg("QR Code Generator/QRCode.svg", scale = 8)

# Create the png
url.png('QR Code Generator/QRCode.png', scale = 6)