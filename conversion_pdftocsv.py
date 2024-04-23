import fitz
import csv

def pdftocsv(pdf, output):
  check= False
  with fitz.open(pdf) as doc:
    with open(output,'w') as file:
      writer= csv.writer(file)
      for page in range(len(doc)):
        tables= doc[page].find_tables()
        table=tables[0]
        table_data= table.extract()
        if not check:
          writer.writerow(table_data[0])
          check= True
        for row in table_data[1:]:
          writer.writerow(row)

pdftocsv("parties.pdf","partiesdata.csv")
pdftocsv("indcomps.pdf","indcompsdata.csv")