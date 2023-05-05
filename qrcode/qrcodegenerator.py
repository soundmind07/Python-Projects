"""
Project Learnings:-
1- used qrcode library of python
2- customised border and box size value to generate customised qr code
3- for color properties i used fill color and back color
4- on scanning this qr code u will be receive a link that takes u to my git hub profile.

"""

import qrcode 
from PIL import Image 

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10, border=4,) 
qr.add_data("https://github.com/soundmind07")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("github.png")
