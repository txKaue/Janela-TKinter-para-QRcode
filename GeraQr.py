import qrcode
from PIL import Image, ImageTk
import qrcode.constants
import tkinter as tk

def CriarQr(url):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img


def GerarImagem(tela, url):
    img = CriarQr(url)
    img_tk = ImageTk.PhotoImage(img)

    label_img = tk.Label(tela, image=img_tk)
    label_img.image = img_tk
    label_img.pack(pady=20)