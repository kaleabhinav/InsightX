import logging
from pdf_reader import extract_text_from_pdf
from text_cleaner import *
from text_parser import parse_sections

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    pdf_path = "data/sample_paper.pdf"
    raw_text = extract_text_from_pdf(pdf_path=pdf_path)
    cleaned_text = clean_text(raw_text)
    parsed = parse_sections(cleaned_text)
    for key, val in parsed.items():
        print(f"{key.upper()}:\n{val}\n{'-'*40}")
