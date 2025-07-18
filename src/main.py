import logging
from extractor.pdf_reader import extract_text_from_pdf


logger = logging.getLogger(__name__)

if __name__ == "__main__":
    pdf_path = "data/sample_paper.pdf"
    text = extract_text_from_pdf(pdf_path=pdf_path)

    print("\n--- Extracted Text ---\n")
    print(text[:1000])
