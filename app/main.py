import barcode
import csv

# working code to create picture
# from barcode.writer import ImageWriter
# ean = barcode.get('ean13', '123456789102', writer=ImageWriter())
# filename = ean.save('ean13')
# filename


confirmation = "XRV29M"

with open('Databased.csv', 'rt') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        for field in row:
            if field == confirmation:
                print row[11]
