import os
import re
import PyPDF2
import pdfplumber


def search_keyword_in_pdf(file_path, keyword):
    pages_with_keyword = []

    with pdfplumber.open(file_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and keyword.lower() in text.lower():
                pages_with_keyword.append(page_number)

    return pages_with_keyword


def extract_pages_to_new_pdf(input_pdf_path, output_pdf_path, pages):
    with open(input_pdf_path, "rb") as input_pdf_file:
        reader = PyPDF2.PdfReader(input_pdf_file)
        writer = PyPDF2.PdfWriter()

        for page_number in pages:
            writer.add_page(reader.pages[page_number])

        with open(output_pdf_path, "wb") as output_pdf_file:
            writer.write(output_pdf_file)


if __name__ == "__main__":
    input_dir = "input"
    output_dir = "output"
    keyword = input("Bitte geben Sie das Stichwort ein: ")
    cleaned_keyword = re.sub(r'\W+', '', keyword)

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            input_pdf_path = os.path.join(input_dir, filename)
            pages = search_keyword_in_pdf(input_pdf_path, keyword)

            if pages:
                print(f"Das Stichwort '{keyword}' wurde in '{filename}' auf den Seiten {pages} gefunden.")
                output_pdf_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_{cleaned_keyword}.pdf")
                extract_pages_to_new_pdf(input_pdf_path, output_pdf_path, pages)
            else:
                print(f"Das Stichwort '{keyword}' wurde in '{filename}' nicht gefunden.")
