from pypdf import PdfReader


def load_pdf(path):
    """
    Load a PDF file and extract text from all pages
    """

    reader = PdfReader(path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text