
import pdfplumber
import os

os.chdir(r'c:\Users\Wilkens\Desktop\Curr\u00edculo')
pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
print("Found:", pdf_files)

with pdfplumber.open(pdf_files[0]) as pdf:
    print(f"Total pages: {len(pdf.pages)}")
    for i, page in enumerate(pdf.pages):
        print(f"\n=== PAGE {i+1} ===")
        t = page.extract_text()
        if t:
            print(t)
        words = page.extract_words()
        if words:
            all_words = ' '.join([w['text'] for w in words])
            print("WORDS:", all_words)
