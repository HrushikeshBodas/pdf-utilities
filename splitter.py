import os
from pdf2image import convert_from_path
from PIL import Image
from fpdf import FPDF

files = []
for (roots, dirs, file_) in os.walk("."):
    files = file_
    break
print("aa", files)
for f in files:
    if f.endswith(".pdf"):
        new_pdf = FPDF()
        new_images = []
        images = convert_from_path("./{}".format(f))
        for image in images:
            w, h = image.size
            midw = w / 2
            midh = h / 2
            # Left, top right, bottom
            new_images.append(image.crop((0, 0, midw, midh)))
            new_images.append(image.crop((midw, 0, w, midh)))
            new_images.append(image.crop((0, midh, midw, h)))
            new_images.append(image.crop((midw, midh, w, h)))
        pdf_name = "split_{}".format(f)
        new_images[0].save(
            pdf_name,
            "PDF",
            resolution=100,
            save_all=True,
            append_images=new_images[1:],
            optimize=True,
            quality=80,
        )
