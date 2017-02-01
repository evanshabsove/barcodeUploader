import barcode

from barcode.writer import ImageWriter
ean = barcode.get('ean13', '123456789102', writer=ImageWriter())
filename = ean.save('ean13')
filename

# def makingBarcode(name, barcode):
#     from barcode.writer import ImageWriter
#     ean = barcode.get(name, barcode, writer=ImageWriter())
#     filename = ean.save(name)
#     filename
#
# makingBarcode("test", '123456789102')
