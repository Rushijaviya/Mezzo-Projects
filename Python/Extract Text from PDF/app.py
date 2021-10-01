# pip install pdfplumber
# importing pdfplumber
import pdfplumber
with pdfplumber.open("Extract Text from PDF\demo.pdf") as pdf:
    length = len(pdf.pages)
    print(f"Total number of Page is {length}.")  # find total pages
    for i in range(1, min(3, length)):  # Print first 2 pages
        text = pdf.pages[i]
        print()
        print(f"Page {i}:")
        print(text.extract_text())  # Extract Text from page
