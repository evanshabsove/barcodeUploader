try:
    import tkinter
except:
    import Tkinter as tkinter

from Tkinter import *
import ttk
import tkMessageBox
import os
import barcode
import win32print
import win32ui
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont, ImageWin, ImageTk
import csv
# top = tkinter.Tk()
# # Code to add widgets will go here...
# -*- mode: python -*-

# Adding csv?
image = 'BADGE DESIGN.png'
csv_path = 'Databased.csv'
# main function that prints off logo
def badgeGenerator(*args):
    confirmation = confirmation_code.get()
    foundBarcode = 1
    with open(csv_path, 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if row[12] == confirmation:
                foundBarcode = row[11]
                name = row[1] + ' ' + row[2] + ' ' +  row[5]



    if foundBarcode == 1:
        tkMessageBox.showerror("Error", "Did not match any codes, try again (CASE SENSATIVE)")
        confirmation_code_entry.delete(0, END)
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
        font = ImageFont.truetype("LiberationMono-Regular.ttf", 26)
        length = len(name)
        name_offset = length*8
        draw.text((1235 - name_offset, 1825),name,(0,0,0),font=font)
        draw.text((435 - name_offset, 1825),name,(0,0,0),font=font)
        img.save(name + 'text.jpg')
        #
        # Constants for GetDeviceCaps
        #
        #
        # HORZRES / VERTRES = printable area
        #
        HORZRES = 8
        VERTRES = 10
        #
        # LOGPIXELS = dots per inch
        #
        LOGPIXELSX = 88
        LOGPIXELSY = 90
        #
        # PHYSICALWIDTH/HEIGHT = total area
        #
        PHYSICALWIDTH = 110
        PHYSICALHEIGHT = 111
        #
        # PHYSICALOFFSETX/Y = left / top margin
        #
        PHYSICALOFFSETX = 112
        PHYSICALOFFSETY = 113

        printer_name = win32print.GetDefaultPrinter ()
        file_name = name + 'text.jpg'

        #
        # You can only write a Device-independent bitmap
        #  directly to a Windows device context; therefore
        #  we need (for ease) to use the Python Imaging
        #  Library to manipulate the image.
        #
        # Create a device context from a named printer
        #  and assess the printable size of the paper.
        #
        hDC = win32ui.CreateDC ()
        hDC.CreatePrinterDC (printer_name)
        printable_area = hDC.GetDeviceCaps (HORZRES), hDC.GetDeviceCaps (VERTRES)
        printer_size = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps (PHYSICALHEIGHT)
        printer_margins = hDC.GetDeviceCaps (PHYSICALOFFSETX), hDC.GetDeviceCaps (PHYSICALOFFSETY)

        #
        # Open the image, rotate it if it's wider than
        #  it is high, and work out how much to multiply
        #  each pixel by to get it as big as possible on
        #  the page without distorting.
        #
        bmp = Image.open (file_name)
        if bmp.size[0] > bmp.size[1]:
          bmp = bmp.rotate (90)

        ratios = [1.0 * printable_area[0] / bmp.size[0], 1.0 * printable_area[1] / bmp.size[1]]
        scale = min (ratios)

        #
        # Start the print job, and draw the bitmap to
        #  the printer device at the scaled size.
        #
        hDC.StartDoc (file_name)
        hDC.StartPage ()

        dib = ImageWin.Dib (bmp)
        scaled_width, scaled_height = [int (scale * i) for i in bmp.size]
        x1 = int ((printer_size[0] - scaled_width) / 2)
        y1 = int ((printer_size[1] - scaled_height) / 2)
        x2 = x1 + scaled_width
        y2 = y1 + scaled_height
        dib.draw (hDC.GetHandleOutput (), (x1, y1, x2, y2))

        hDC.EndPage ()
        hDC.EndDoc ()
        hDC.DeleteDC ()
        os.remove('out.jpg')
        os.remove(name + ".png")
        # os.remove(name + 'text.jpg')
        confirmation_code_entry.delete(0, END)


# tkinter program

# Method to make it load full screen every time
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

# method for giving character limit
def character_limit(confirmation_code):
    if len(confirmation_code.get()) > 0:
        confirmation_code.set(confirmation_code.get()[:6])


# main root calling method to make it go full screen
root = Tk()
root.configure()
root.title("Print your badge")
app=FullScreenApp(root)

# Ways to style button and frame, mostly for changing colours
gui_style = ttk.Style()
gui_style.configure('My.TButton')
gui_style.configure('My.TFrame')

# Main frame styling mostly for changing padding
mainframe = ttk.Frame(root, padding="350 100 0 0", style='My.TFrame')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Labels
img = ImageTk.PhotoImage(Image.open("logo.png"))
image_panel = Label(mainframe, image = img, pady=20)
image_panel.grid(column=1, row=0)
first_text = Label(mainframe, text="Media Badge Self-Serve Kiosk", font=("Helvetica", 42), fg="red", pady=20)
first_text.grid(column=1, row=1)
second_text = Label(mainframe, text="You should have recieved your confirmation code by email. Enter it below.", font=("Helvetica", 28), fg="black", pady=20)
second_text.grid(column=1, row=2)
fourth_text = Label(mainframe, text="If you do not have a code, please see our check-in desk.", font=("Helvetica", 28), fg="red", pady=20)
fourth_text.grid(column=1, row=4)

# entry/submit button
confirmation_code = StringVar()
confirmation_code_entry = ttk.Entry(mainframe, font = "Helvetica 44", justify='center', width=12, textvariable=confirmation_code)
confirmation_code_entry.grid(column=1, row=5, sticky=(W, E))
b = Button(mainframe, text="Submit", font = "Helvetica 38", width=10, command=badgeGenerator)
b.grid(column = 1, row = 6)
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

confirmation_code.trace("w", lambda *args: character_limit(confirmation_code))

confirmation_code_entry.focus()
root.bind('<Return>', badgeGenerator)

root.mainloop()
