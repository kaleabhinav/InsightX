import re
import logging

logger = logging.getLogger(__name__)

def parse_sections(text: str) -> dict:
    logger.info("Parsing cleaned text into sections...")

    sections = {
        "title": None,
        "authors": None,
        "doi": None,
        "abstract": None,
        "body": None
    }

    try:
        lines = text.splitlines()
        full_text = " ".join(lines)

        # ---------- TITLE ----------
        # Look for a line with 5+ words that doesn't look like a header
        for line in lines[:15]:
            if len(line.split()) > 4 and not re.search(r'abstract|corresponding|author', line.lower()):
                sections["title"] = line.strip()
                break

        # ---------- DOI ----------
        doi_match = re.search(r'10\.\d{4,9}/[-._;()/:A-Za-z0-9]+', full_text)
        if doi_match:
            sections["doi"] = doi_match.group(0).rstrip('/')

        # ---------- AUTHORS ----------
        # Grab all possible names (First Last)
        name_matches = re.findall(r'([A-Z][a-z]+\s[A-Z][a-z]+)', full_text)
        ignore_list = {"Pharmaceutical Research", "British Journal", "Muscle Length", "Lower Extremity"}
        filtered_names = [name for name in name_matches if name not in ignore_list]
        if filtered_names:
            sections["authors"] = ", ".join(sorted(set(filtered_names), key=filtered_names.index))

        # ---------- ABSTRACT ----------
        abstract_match = re.search(r'(?i)abstract[:\s]*([\s\S]{100,1000}?)\n[A-Z]', text)
        if abstract_match:
            sections["abstract"] = abstract_match.group(1).strip()
        else:
            # Fallback: Grab the paragraph after the title
            if sections["title"]:
                try:
                    title_index = lines.index(sections["title"])
                    potential_abstract = "\n".join(lines[title_index + 1:title_index + 6])
                    if len(potential_abstract.split()) > 40:
                        sections["abstract"] = potential_abstract.strip()
                except Exception as e:
                    logger.warning(f"Could not fallback to abstract: {e}")

        # ---------- BODY ----------
        if sections["abstract"]:
            body_start_index = full_text.find(sections["abstract"]) + len(sections["abstract"])
            body = full_text[body_start_index:].strip()
            if len(body) > 200:
                sections["body"] = body

        logger.info("Parsing complete.")
        return sections

    except Exception as e:
        logger.error(f"Error during parsing: {e}")
        return sections
