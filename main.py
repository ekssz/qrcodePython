import pyqrcode
from pyqrcode import QRCode

link = "https://discord.gg/CUQhNBzRAs"

url = pyqrcode.create(link)

url.svg("dsqr.svg", scale = 8)
