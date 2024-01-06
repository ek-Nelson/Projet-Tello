from djitellopy import Tello
import qrcode
import qrcode.image.pil
import time

startcounter = 0

    # Connection to Tello 


def generate_qr_code(url, filename):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)
    image = qr.make_image(image_factory=qrcode.image.pil.PilImage)
    image.save(filename)


# Exemple d'utilisation
generate_qr_code('mvr_test', "move_right.jpeg") 