import barcode
from barcode.writer import ImageWriter
import csv


confirmation = "XRV29M"

with open('Databased.csv', 'rt') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        for field in row:
            if field == confirmation:
                foundBarcode = row[11]
                name = row[1] + row[2]

print foundBarcode
print name


CODE = barcode.get_barcode_class('code128')
code = CODE(foundBarcode, writer=ImageWriter())
fullname = code.save(name)
