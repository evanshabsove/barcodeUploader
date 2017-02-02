import os
import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont
import csv

# top.mainloop()
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

Logo = resource_path("BADGE DESIGN.png")


def badgeGenerator(confirmation):

    foundBarcode = 1
    with open('Databased.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            for field in row:
                if field == confirmation:
                    foundBarcode = row[11]
                    name = row[1] + ' ' + row[2]


    if foundBarcode == 1:
        print "nope"
    else:
        CODE = barcode.get_barcode_class('code128')
        code = CODE(foundBarcode, writer=ImageWriter())
        fullname = code.save(name)

        badge = Image.open('BADGE DESIGN.png', 'r')
        img = Image.open(name + ".png", 'r')
        img_w, img_h = img.size
        badge_w, badge_h = badge.size
        offset = ((badge_w - img_w)/2 + 400, (badge_h - img_h)/2 + 670)
        offset2 = ((badge_w - img_w)/2 - 400, (badge_h - img_h)/2 + 670)
        badge.paste(img, offset)
        badge.paste(img, offset2)
        badge.save('out.png')


badgeGenerator('BKPVR5')
