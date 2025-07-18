import logging
from PyPDF2 import PdfReader

logger = logging.getLogger(__name__)

def extract_text_from_pdf(pdf_path: str) -> str:

    try:
        logger.info(f"Reading PDF from : {pdf_path}")
        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:

            text += page.extract_text() or ""
        
        logger.info("PDF text extraction successful")
        return text
    
    except Exception as e:

        logger.error(f"Failed to read PDF: {e}")

        return ""
    

