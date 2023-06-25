from sys import argv
from os import path, mkdir
from docx import Document
from docx.shared import Cm
from pdf2image import convert_from_path

if len(argv) < 2:
    raise RuntimeError("Expected path to PDF file as argument")

if not path.exists("./images"):
    mkdir("./images")

doc = Document()

for count, page in enumerate(convert_from_path(argv[1], 500)):
    page.save(f"./images/page_{count}.jpg", "JPEG")
    doc.add_picture(f"./images/page_{count}.jpg", width=Cm(15))

doc.save("out.docx")