import logging
import re

logger = logging.getLogger(__name__)

def clean_text(raw_text: str) -> str:

    try:
        logger.info("Cleaning extracted text...")

        # 1. Remove email addresses
        text = re.sub(r'\S+@\S+', '', raw_text)

        # 2. Remove long lines of underscores (usually separators)
        text = re.sub(r'_+', '', text)

        # 3. Fix hyphenated line breaks (e.g., "physio-\ntherapy" → "physiotherapy")
        text = re.sub(r'-\s*\n\s*', '', text)

        # 4. Replace multiple line breaks with a single newline
        text = re.sub(r'\n+', '\n', text)

        # 5. Normalize spacing: collapse multiple spaces/tabs into one
        text = re.sub(r'[ \t]+', ' ', text)

        # 6. Optional: remove known boilerplate sections if applicable
        # Example: Remove author contributions section
        text = re.sub(
            r"Authors[’'] contributions.*?Article Information",
            '',
            text,
            flags=re.DOTALL | re.IGNORECASE
        )

        logger.info("Text cleaning complete.")
        return text.strip()

    except Exception as e:
        logger.error(f"Error during text cleaning: {e}")
        return raw_text
