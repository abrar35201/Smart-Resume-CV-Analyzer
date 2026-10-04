import re
import PyPDF2
import docx

# Extract text from PDF

def extract_text_from_pdf(file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(file)

    for page in pdf_reader.pages:
        text += page.extract_text()

    return text

# Extract text from DOCX

def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = ""

    for para in doc.paragraphs:
        text += para.text + " "

    return text

# Clean text

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    text = re.sub(r'\s+', ' ', text)

    return text