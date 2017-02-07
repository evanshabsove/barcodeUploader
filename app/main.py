try:
    import tkinter
except:
    import Tkinter as tkinter

from Tkinter import *
import ttk
import tkMessageBox
import os
import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont
import csv
# top = tkinter.Tk()
# # Code to add widgets will go here...
# -*- mode: python -*-

# Adding csv?
image = 'BADGE DESIGN.png'
csv_path = 'Databased.csv'
# main function that prints off logo
def badgeGenerator(*args):
    confirmation = confirmation_code_entry.get("1.0",END)
    confirmation = str(confirmation)
    confirmation = confirmation.rstrip()
    foundBarcode = 1
    with open(csv_path, 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            for field in row:
                if field == confirmation:
                    foundBarcode = row[11]
                    name = row[1] + ' ' + row[2]



    if foundBarcode == 1:
        tkMessageBox.showerror("Error", "Did not match any codes, try again (CASE SENSATIVE)")
    else:
        CODE = barcode.get_barcode_class('code128')
        code = CODE(foundBarcode, writer=ImageWriter())
        fullname = code.save(name)
        badge = Image.open(image, 'r')
        img = Image.open(name + ".png", 'r')
        img_w, img_h = img.size
        badge_w, badge_h = badge.size
        offset = ((badge_w - img_w)/2 + 400, (badge_h - img_h)/2 + 670)
        offset2 = ((badge_w - img_w)/2 - 400, (badge_h - img_h)/2 + 670)
        badge.paste(img, offset)
        badge.paste(img, offset2)
        badge.save('out.jpg')
        img = Image.open('out.jpg')
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Aaargh.ttf", 26)
        draw.text((1165, 1825),name,(0,0,0),font=font)
        draw.text((365, 1825),name,(0,0,0),font=font)
        img.save('outtext.jpg')


# tkinter program
root = Tk()
root.title("Print your badge")

mainframe = ttk.Frame(root, padding="100 100 100 100")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

confirmation_code = StringVar()

confirmation_code_entry = Text(mainframe, width=20)
confirmation_code_entry.grid(column=2, row=1, sticky=(W, E))
b = ttk.Button(mainframe, text="Submit", command=badgeGenerator)
b.grid(column = 1, row = 1)
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

confirmation_code_entry.focus()
root.bind('<Return>', badgeGenerator)

root.mainloop()
