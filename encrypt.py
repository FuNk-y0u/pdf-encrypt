from pypdf import PdfReader, PdfWriter
import os

PATH = "in"

pdfs = os.listdir(PATH)
total = len(pdfs)
print(f"TOTAL PDFS: {total}")
PASS = "[your password here]"
count = 0

for pdf in pdfs:
    reader = PdfReader(f"in/{pdf}")
    writer = PdfWriter()
    writer.append_pages_from_reader(reader)
    writer.encrypt(PASS)

    with open(f"out/{pdf}", "wb") as out_file:
        writer.write(out_file)
    
    count += 1
    print(f"{count}/{total}")
    

