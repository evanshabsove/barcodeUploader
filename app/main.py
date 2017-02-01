import barcode
from barcode.writer import ImageWriter
from PIL import Image
import csv


confirmation = "XRV29M"

with open('Databased.csv', 'rt') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        for field in row:
            if field == confirmation:
                foundBarcode = row[11]
                name = row[1] + ' ' + row[2]


CODE = barcode.get_barcode_class('code128')
code = CODE(foundBarcode, writer=ImageWriter())
fullname = code.save(name)

badge = Image.open('badge2017.png', 'r')
img = Image.open(name + ".png", 'r')
img_w, img_h = img.size
badge_w, badge_h = badge.size
